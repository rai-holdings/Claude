---
name: tao-media
description: >
  Tạo hình ảnh và video AI đẳng cấp điện ảnh từ một ý tưởng ngắn — gõ một ý là tạo ra luôn.
  Use when the user asks to create/generate an image, picture, photo, artwork, video, clip,
  animation, or visual content from an idea — in Vietnamese or English (tạo ảnh, tạo video,
  vẽ, làm clip, generate image, make a video). Automatically enhances the idea into a
  professional cinematic prompt, routes to the best model (Veo 3.1, Kling, FLUX.2, Imagen 4,
  GPT Image), generates, and delivers the file.
---

# Tạo Media Đẳng Cấp (One-Idea → Perfect Image/Video)

Biến MỘT ý tưởng ngắn của người dùng thành hình ảnh/video chất lượng cao nhất, hoàn toàn tự động.
KHÔNG hỏi lại người dùng trừ khi thiếu API key. Toàn bộ pipeline chạy trong một lượt.
Mặc định chạy **Perfect Mode**: tạo → tự xem lại → tự chấm điểm → tự sửa → tạo lại đến khi đạt chuẩn.

## Quy trình (làm đúng thứ tự, không bỏ bước)

### Bước 1 — Phân loại ý tưởng
Đọc ý tưởng và quyết định:
- **video**: ý tưởng có chuyển động, thời gian, hành động, cảnh quay, hoặc người dùng nói
  "video/clip/phim/quay/animation/chuyển động".
- **image**: mặc định cho mọi trường hợp còn lại (chân dung, phong cảnh, logo, poster, sản phẩm…).
- Nếu người dùng muốn CẢ HAI thì tạo ảnh trước, video sau.

### Bước 2 — Nâng cấp prompt (bắt buộc — đây là thứ tạo nên "đẳng cấp")
Đọc `references/prompt-guide.md` rồi viết lại ý tưởng thành prompt TIẾNG ANH chuyên nghiệp:
- Ảnh: subject + action + environment + lighting + camera/lens + composition + style + mood + chi tiết chất liệu.
- Video: thêm camera movement, pacing, và audio cues (Veo 3.1 tạo được âm thanh đồng bộ).
- Giữ đúng ý gốc của người dùng, chỉ làm giàu chi tiết. Tên riêng/chữ cần hiển thị trong ảnh thì giữ nguyên văn, đặt trong ngoặc kép.
- Chọn aspect ratio hợp nội dung: chân dung/TikTok → 9:16, phong cảnh/cinematic → 16:9, logo/avatar → 1:1, poster → 3:4.

### Bước 3 — Sinh media
Chạy script (Python 3, không cần cài thêm thư viện):

```bash
python3 .claude/skills/tao-media/scripts/generate.py "ENHANCED PROMPT" \
  --type image|video --ar 16:9 [--duration 8] [--resolution 1080p] [--model <endpoint>] \
  [--count N] [--image <keyframe.png>] [--seed N] [--negative "..."]
```

- `--image`: ảnh tham chiếu (đường dẫn hoặc URL) → tự chuyển sang image-to-video (Veo 3.1/Kling).
- `--seed`: giữ seed của bản đẹp khi chỉ sửa lỗi nhỏ (FLUX) — bảo toàn phần đã ưng.
- `--negative`: negative prompt cho Kling.

- Script tự chọn provider theo API key có sẵn: `FAL_KEY` (ưu tiên — nhiều model nhất) →
  `GEMINI_API_KEY` (Imagen 4 / Veo 3.1) → `OPENAI_API_KEY` (GPT Image).
- Script tự fallback qua chuỗi model nếu một endpoint lỗi. Chỉ dùng `--model` khi cần model
  cụ thể (xem `references/models.md` để chọn theo nhu cầu: photorealism, typography, giá rẻ, tốc độ).
- Video có thể mất 1–6 phút — cứ để script chạy (timeout mặc định của Bash tool có thể cần tăng lên 600000).
- Dòng cuối stdout là JSON: `{"files": [...], "model": "...", "provider": "..."}`.

### Bước 4 — Perfect Mode: tự chấm & tinh chỉnh (bắt buộc với ảnh)
Đọc `references/refine-checklist.md` rồi lặp:
1. Mở file ảnh vừa tạo bằng tool **Read** (Read hiển thị được ảnh) và chấm theo rubric 10 điểm.
2. Đạt **≥ 9/10** → sang Bước 5. Chưa đạt → sửa prompt đúng theo bảng "cách sửa lỗi"
   (chỉ sửa 1–3 điểm yếu nhất, giữ phần đã đẹp; FLUX có thể giữ `--seed`) và chạy lại script.
3. Tối đa **3 vòng**. Hết vòng chưa đạt → giao bản điểm cao nhất, nói rõ hạn chế còn lại.
- Với ảnh quan trọng (poster, logo, chân dung): tạo `--count 2` ngay vòng đầu và chấm cả hai, lấy bản tốt hơn làm nền tinh chỉnh.

**Video chất lượng đỉnh (Perfect Video Pipeline)** — dùng khi người dùng muốn "đẹp nhất/hoàn hảo/quảng cáo":
1. Tạo keyframe ẢNH theo vòng lặp trên cho đạt ≥ 9/10.
2. Animate keyframe: `generate.py "MOTION + AUDIO prompt" --type video --image <keyframe>` —
   script tự route sang Veo 3.1 / Kling image-to-video. Prompt lúc này chỉ tả chuyển động + âm thanh.
3. Nếu có `ffmpeg`: trích vài frame của video ra chấm lại; lỗi nặng → chỉnh motion prompt, tạo lại (tối đa 2 vòng).
Video nhanh/thường: gọi text-to-video thẳng (Bước 3) là đủ.

### Bước 5 — Giao kết quả
- Gửi file cho người dùng bằng tool `SendUserFile` với `display: "render"`.
- Trả lời bằng ngôn ngữ của người dùng, nêu: model đã dùng, số vòng tinh chỉnh + điểm rubric,
  prompt đã nâng cấp (ngắn gọn), và gợi ý 1–2 biến thể tiếp theo (đổi style, đổi tỉ lệ, làm video từ ảnh…).

## Khi thiếu API key
Nếu script báo thiếu key, hướng dẫn ngắn gọn:
1. **fal.ai** (khuyên dùng): đăng ký tại https://fal.ai/dashboard/keys → `export FAL_KEY="..."`
2. **Google AI Studio**: https://aistudio.google.com/apikey → `export GEMINI_API_KEY="..."`
3. **OpenAI**: https://platform.openai.com/api-keys → `export OPENAI_API_KEY="..."`

Rồi dừng lại chờ người dùng cung cấp key — không tự bịa kết quả.

## Nguyên tắc chất lượng
- Không bao giờ gửi prompt thô của người dùng thẳng vào model — luôn nâng cấp (Bước 2).
- Không hạ cấp model để tiết kiệm trừ khi người dùng yêu cầu "rẻ/nhanh".
- Nội dung người thật, thương hiệu thật, hoặc nhạy cảm: từ chối lịch sự theo chính sách model.
- Kết quả xấu/lỗi: thử lại 1 lần với prompt tinh chỉnh trước khi báo người dùng.
