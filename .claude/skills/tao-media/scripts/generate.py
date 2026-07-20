#!/usr/bin/env python3
"""One-idea -> instant image/video generator.

Pure standard library (urllib) — no pip install needed.

Providers (auto-detected by env var, in priority order):
  1. FAL_KEY          -> fal.ai queue API   (Veo 3.1, Kling 3.0, FLUX.2, Imagen 4, ...)
  2. GEMINI_API_KEY   -> Google AI          (Imagen 4, Veo 3.1)
  3. OPENAI_API_KEY   -> OpenAI             (GPT Image; Sora 2 until API sunset 2026-09)

Usage:
  python3 generate.py "cinematic prompt" --type video --ar 16:9 --duration 8
  python3 generate.py "portrait prompt"  --type image --ar 3:4 --count 2

Last stdout line is machine-readable JSON:
  {"files": ["..."], "model": "...", "provider": "..."}
"""

import argparse
import base64
import json
import mimetypes
import os
import re
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

# ---------------------------------------------------------------------------
# Model routing — ordered fallback chains (best first). Endpoint IDs verified
# against fal.ai docs as of 2026-07; the chain absorbs endpoint drift.
# ---------------------------------------------------------------------------
FAL_IMAGE_CHAIN = [
    "fal-ai/flux-2-pro",
    "fal-ai/flux-pro/v1.1-ultra",
    "fal-ai/imagen4/preview",
    "fal-ai/flux/dev",
]
FAL_VIDEO_CHAIN = [
    "fal-ai/veo3.1",
    "fal-ai/kling-video/v3/pro/text-to-video",
    "fal-ai/kling-video/v2.1/master/text-to-video",
    "fal-ai/minimax/hailuo-02/standard/text-to-video",
]
FAL_I2V_CHAIN = [
    "fal-ai/veo3.1/image-to-video",
    "fal-ai/kling-video/v3/pro/image-to-video",
    "fal-ai/kling-video/v2.1/master/image-to-video",
    "fal-ai/minimax/hailuo-02/standard/image-to-video",
]

VIDEO_HINTS = re.compile(
    r"\b(video|clip|phim|film|quay|animation|animate|chuy[eê]?n\s*đ[oộ]ng|"
    r"c[aả]nh\s*quay|footage|cinemagraph|timelapse|slow\s*motion)\b",
    re.IGNORECASE,
)

POLL_INTERVAL = 4
POLL_TIMEOUT = 15 * 60


def log(msg):
    print(msg, file=sys.stderr, flush=True)


def http(url, method="GET", headers=None, body=None, timeout=120):
    data = None
    headers = dict(headers or {})
    if body is not None:
        data = json.dumps(body).encode()
        headers.setdefault("Content-Type", "application/json")
    req = urllib.request.Request(url, data=data, headers=headers, method=method)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return json.loads(r.read().decode())


def download(url, dest, headers=None):
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req, timeout=300) as r, open(dest, "wb") as f:
        while True:
            chunk = r.read(1 << 16)
            if not chunk:
                break
            f.write(chunk)
    return dest


def out_path(out_dir, kind, ext, idx=0):
    stamp = time.strftime("%Y%m%d_%H%M%S")
    suffix = f"_{idx + 1}" if idx else ""
    return str(Path(out_dir) / f"{kind}_{stamp}{suffix}{ext}")


def ext_from_url(url, fallback):
    path = url.split("?")[0]
    ext = Path(path).suffix
    return ext if ext and len(ext) <= 5 else fallback


def image_ref_to_url(ref):
    """Local image file -> base64 data URI; http(s)/data URLs pass through."""
    if ref.startswith(("http://", "https://", "data:")):
        return ref
    p = Path(ref)
    if not p.is_file():
        raise RuntimeError(f"image not found: {ref}")
    mime = mimetypes.guess_type(p.name)[0] or "image/png"
    return f"data:{mime};base64,{base64.b64encode(p.read_bytes()).decode()}"


# ---------------------------------------------------------------------------
# fal.ai
# ---------------------------------------------------------------------------
def fal_payload(model, prompt, args):
    """Per-model-family payloads; unknown models get a safe generic body."""
    p = {"prompt": prompt}
    if args.image:
        p["image_url"] = image_ref_to_url(args.image)
    if "veo3" in model:
        p.update(
            aspect_ratio=args.ar,
            duration=f"{args.duration}s",
            resolution=args.resolution,
            generate_audio=not args.no_audio,
        )
    elif "kling-video" in model:
        p.update(duration=str(min(max(args.duration, 5), 10)), aspect_ratio=args.ar)
        if args.negative:
            p["negative_prompt"] = args.negative
    elif "hailuo" in model:
        p.update(duration=str(6 if args.duration <= 6 else 10))
    elif "flux/dev" in model:
        size_map = {
            "1:1": "square_hd", "16:9": "landscape_16_9", "9:16": "portrait_16_9",
            "4:3": "landscape_4_3", "3:4": "portrait_4_3",
        }
        p.update(image_size=size_map.get(args.ar, "landscape_16_9"),
                 num_images=args.count)
        if args.seed is not None:
            p["seed"] = args.seed
    elif "flux" in model or "imagen" in model:
        p.update(aspect_ratio=args.ar, num_images=args.count)
        if args.seed is not None:
            p["seed"] = args.seed
    else:
        p.update(aspect_ratio=args.ar)
    return p


def fal_generate(model, prompt, args, key):
    headers = {"Authorization": f"Key {key}"}
    submit = http(
        f"https://queue.fal.run/{model}",
        method="POST",
        headers=headers,
        body=fal_payload(model, prompt, args),
    )
    status_url = submit.get("status_url")
    response_url = submit.get("response_url")
    if not status_url:
        raise RuntimeError(f"fal submit returned no status_url: {submit}")

    log(f"[fal] queued on {model} (request {submit.get('request_id', '?')})")
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        st = http(f"{status_url}?logs=0", headers=headers)
        state = st.get("status")
        if state == "COMPLETED":
            break
        if state in ("FAILED", "CANCELLED", "ERROR"):
            raise RuntimeError(f"fal job {state}: {st}")
        time.sleep(POLL_INTERVAL)
    else:
        raise RuntimeError(f"fal job timed out after {POLL_TIMEOUT}s")

    result = http(response_url, headers=headers)
    urls = []
    for k in ("video", "image"):
        item = result.get(k)
        if isinstance(item, dict) and item.get("url"):
            urls.append(item["url"])
    for k in ("images", "videos"):
        for item in result.get(k) or []:
            if isinstance(item, dict) and item.get("url"):
                urls.append(item["url"])
    if not urls:
        raise RuntimeError(f"no media url in fal response: {json.dumps(result)[:500]}")

    files = []
    default_ext = ".mp4" if args.type == "video" else ".png"
    for i, u in enumerate(urls):
        dest = out_path(args.out, args.type, ext_from_url(u, default_ext), i)
        files.append(download(u, dest))
    return files


# ---------------------------------------------------------------------------
# Google Gemini API (Imagen 4 / Veo 3.1)
# ---------------------------------------------------------------------------
GEMINI_BASE = "https://generativelanguage.googleapis.com/v1beta"

# (model, api_method) — newest first; older Imagen predict models are gated
# for new users, so the chain falls through automatically.
GEMINI_IMAGE_CHAIN = [
    ("gemini-3-pro-image", "generateContent"),
    ("gemini-3.1-flash-image", "generateContent"),
    ("gemini-2.5-flash-image", "generateContent"),
    ("imagen-4.0-ultra-generate-001", "predict"),
    ("imagen-4.0-generate-001", "predict"),
    ("imagen-4.0-fast-generate-001", "predict"),
]


def _save_b64_images(items, args):
    """items: [(b64, mime)] -> saved file paths."""
    files = []
    for i, (b64, mime) in enumerate(items):
        ext = mimetypes.guess_extension(mime or "image/png") or ".png"
        dest = out_path(args.out, "image", ext, i)
        Path(dest).write_bytes(base64.b64decode(b64))
        files.append(dest)
    return files


def gemini_image_once(model, method, prompt, args, key):
    headers = {"x-goog-api-key": key}
    if method == "generateContent":
        body = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["TEXT", "IMAGE"],
                "imageConfig": {"aspectRatio": args.ar},
            },
        }
        items = []
        for _ in range(args.count):
            r = http(f"{GEMINI_BASE}/models/{model}:generateContent",
                     method="POST", headers=headers, body=body, timeout=300)
            for cand in r.get("candidates", []):
                for part in cand.get("content", {}).get("parts", []):
                    blob = part.get("inlineData")
                    if blob and blob.get("data"):
                        items.append((blob["data"], blob.get("mimeType")))
        files = _save_b64_images(items, args)
    else:
        r = http(
            f"{GEMINI_BASE}/models/{model}:predict",
            method="POST", headers=headers,
            body={"instances": [{"prompt": prompt}],
                  "parameters": {"sampleCount": args.count,
                                 "aspectRatio": args.ar}},
            timeout=300,
        )
        files = _save_b64_images(
            [(p["bytesBase64Encoded"], p.get("mimeType"))
             for p in r.get("predictions", []) if p.get("bytesBase64Encoded")],
            args)
    if not files:
        raise RuntimeError(f"{model} returned no images")
    return files


def gemini_image(prompt, args, key):
    chain = ([(args.model, "generateContent" if "gemini" in args.model
               else "predict")] if args.model else GEMINI_IMAGE_CHAIN)
    last = None
    for model, method in chain:
        try:
            return gemini_image_once(model, method, prompt, args, key), model
        except (urllib.error.HTTPError, RuntimeError) as e:
            detail = ""
            if isinstance(e, urllib.error.HTTPError):
                try:
                    detail = e.read().decode()[:200]
                except Exception:
                    pass
            log(f"[gemini] {model} failed: {e} {detail} -> trying next")
            last = e
    raise RuntimeError(f"all gemini image models failed: {last}")


def gemini_video(prompt, args, key):
    headers = {"x-goog-api-key": key}
    instance = {"prompt": prompt}
    if args.image:
        p = Path(args.image)
        if p.is_file():
            instance["image"] = {
                "bytesBase64Encoded": base64.b64encode(p.read_bytes()).decode(),
                "mimeType": mimetypes.guess_type(p.name)[0] or "image/png",
            }
    op = http(
        f"{GEMINI_BASE}/models/veo-3.1-generate-preview:predictLongRunning",
        method="POST",
        headers=headers,
        body={"instances": [instance],
              "parameters": {"aspectRatio": args.ar, "resolution": args.resolution}},
    )
    name = op["name"]
    log(f"[gemini] Veo operation {name}")
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        op = http(f"{GEMINI_BASE}/{name}", headers=headers)
        if op.get("done"):
            break
        time.sleep(POLL_INTERVAL)
    else:
        raise RuntimeError("Veo operation timed out")
    if "error" in op:
        raise RuntimeError(f"Veo failed: {op['error']}")

    videos = (op.get("response", {}).get("generateVideoResponse", {})
              .get("generatedSamples", []))
    if not videos:  # alternate response shape
        videos = op.get("response", {}).get("videos", [])
    files = []
    for i, v in enumerate(videos):
        uri = (v.get("video") or {}).get("uri") or v.get("uri")
        if not uri:
            continue
        dest = out_path(args.out, "video", ".mp4", i)
        files.append(download(uri, dest, headers=headers))
    if not files:
        raise RuntimeError(f"Veo returned no video: {json.dumps(op)[:500]}")
    return files


# ---------------------------------------------------------------------------
# OpenAI (GPT Image; Sora 2 — API sunsets 2026-09, kept as last resort)
# ---------------------------------------------------------------------------
def openai_image(prompt, args, key):
    size_map = {"1:1": "1024x1024", "16:9": "1536x1024", "9:16": "1024x1536",
                "4:3": "1536x1024", "3:4": "1024x1536"}
    r = http(
        "https://api.openai.com/v1/images/generations",
        method="POST",
        headers={"Authorization": f"Bearer {key}"},
        body={"model": "gpt-image-1", "prompt": prompt, "n": args.count,
              "size": size_map.get(args.ar, "1024x1024")},
    )
    files = []
    for i, item in enumerate(r.get("data", [])):
        if item.get("b64_json"):
            dest = out_path(args.out, "image", ".png", i)
            Path(dest).write_bytes(base64.b64decode(item["b64_json"]))
            files.append(dest)
        elif item.get("url"):
            dest = out_path(args.out, "image", ".png", i)
            files.append(download(item["url"], dest))
    if not files:
        raise RuntimeError(f"GPT Image returned nothing: {json.dumps(r)[:500]}")
    return files


def openai_video(prompt, args, key):
    headers = {"Authorization": f"Bearer {key}"}
    job = http("https://api.openai.com/v1/videos", method="POST", headers=headers,
               body={"model": "sora-2", "prompt": prompt,
                     "seconds": str(args.duration)})
    vid = job["id"]
    log(f"[openai] Sora job {vid}")
    deadline = time.time() + POLL_TIMEOUT
    while time.time() < deadline:
        job = http(f"https://api.openai.com/v1/videos/{vid}", headers=headers)
        if job.get("status") == "completed":
            break
        if job.get("status") in ("failed", "cancelled"):
            raise RuntimeError(f"Sora job failed: {job}")
        time.sleep(POLL_INTERVAL)
    else:
        raise RuntimeError("Sora job timed out")
    dest = out_path(args.out, "video", ".mp4")
    return [download(f"https://api.openai.com/v1/videos/{vid}/content", dest,
                     headers=headers)]


# ---------------------------------------------------------------------------
# main
# ---------------------------------------------------------------------------
NO_KEY_MSG = """\
Chưa có API key. Cần MỘT trong các key sau (ưu tiên theo thứ tự):
  export FAL_KEY="..."         # https://fal.ai/dashboard/keys  (khuyên dùng)
  export GEMINI_API_KEY="..."  # https://aistudio.google.com/apikey
  export OPENAI_API_KEY="..."  # https://platform.openai.com/api-keys
"""


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("prompt")
    ap.add_argument("--type", choices=["auto", "image", "video"], default="auto")
    ap.add_argument("--ar", default=None, help="aspect ratio, e.g. 16:9")
    ap.add_argument("--duration", type=int, default=8, help="video seconds")
    ap.add_argument("--resolution", default="1080p", choices=["720p", "1080p", "4k"])
    ap.add_argument("--count", type=int, default=1, help="number of images")
    ap.add_argument("--model", default=None, help="explicit endpoint/model id")
    ap.add_argument("--provider", choices=["auto", "fal", "gemini", "openai"],
                    default="auto")
    ap.add_argument("--no-audio", action="store_true")
    ap.add_argument("--image", default=None,
                    help="reference image (path or URL) -> image-to-video / editing")
    ap.add_argument("--seed", type=int, default=None,
                    help="seed for reproducible refinement (FLUX)")
    ap.add_argument("--negative", default=None, help="negative prompt (Kling)")
    ap.add_argument("--out", default="media-output")
    args = ap.parse_args()

    if args.type == "auto":
        args.type = ("video" if args.image or VIDEO_HINTS.search(args.prompt)
                     else "image")
        log(f"[auto] detected type: {args.type}")
    if args.ar is None:
        args.ar = "16:9" if args.type == "video" else "1:1"
    Path(args.out).mkdir(parents=True, exist_ok=True)

    fal_key = os.environ.get("FAL_KEY")
    gemini_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    openai_key = os.environ.get("OPENAI_API_KEY")

    order = []
    if args.provider in ("auto", "fal") and fal_key:
        order.append("fal")
    if args.provider in ("auto", "gemini") and gemini_key:
        order.append("gemini")
    if args.provider in ("auto", "openai") and openai_key:
        order.append("openai")
    if not order:
        log(NO_KEY_MSG)
        sys.exit(2)

    errors = []
    for provider in order:
        try:
            if provider == "fal":
                if args.model:
                    chain = [args.model]
                elif args.type == "video":
                    chain = FAL_I2V_CHAIN if args.image else FAL_VIDEO_CHAIN
                else:
                    chain = FAL_IMAGE_CHAIN
                for model in chain:
                    try:
                        files = fal_generate(model, args.prompt, args, fal_key)
                        print(json.dumps({"files": files, "model": model,
                                          "provider": "fal"}))
                        return
                    except (urllib.error.HTTPError, RuntimeError) as e:
                        detail = ""
                        if isinstance(e, urllib.error.HTTPError):
                            try:
                                detail = e.read().decode()[:300]
                            except Exception:
                                pass
                        log(f"[fal] {model} failed: {e} {detail} -> trying next")
                        errors.append(f"fal/{model}: {e}")
                continue
            if provider == "gemini":
                fn = gemini_video if args.type == "video" else gemini_image
                model = ("veo-3.1-generate-preview" if args.type == "video"
                         else "gemini-image")
            else:
                fn = openai_video if args.type == "video" else openai_image
                model = "sora-2" if args.type == "video" else "gpt-image-1"
            files = fn(args.prompt, args,
                       gemini_key if provider == "gemini" else openai_key)
            if isinstance(files, tuple):
                files, model = files
            print(json.dumps({"files": files, "model": model, "provider": provider}))
            return
        except (urllib.error.HTTPError, urllib.error.URLError, RuntimeError,
                KeyError) as e:
            detail = ""
            if isinstance(e, urllib.error.HTTPError):
                try:
                    detail = e.read().decode()[:300]
                except Exception:
                    pass
            log(f"[{provider}] failed: {e} {detail}")
            errors.append(f"{provider}: {e}")

    log("Tất cả provider đều lỗi:\n  " + "\n  ".join(errors))
    sys.exit(1)


if __name__ == "__main__":
    main()
