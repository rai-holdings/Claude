# Bảng định tuyến model (cập nhật 07/2026)

Script tự fallback theo chuỗi mặc định. Chỉ truyền `--model` khi cần chuyên biệt.

## Video (qua fal.ai — `FAL_KEY`)

| Nhu cầu | Model | Endpoint | Ghi chú |
|---|---|---|---|
| **Mặc định — điện ảnh nhất** | Veo 3.1 | `fal-ai/veo3.1` | 720p–4K, âm thanh đồng bộ, prompt adherence tốt nhất, ~$0.15–0.40/s |
| Chuyển động phức tạp, giá tốt | Kling 3.0 Pro | `fal-ai/kling-video/v3/pro/text-to-video` | ~$0.10/s, cinematic lighting, multi-shot |
| Ổn định, rẻ | Kling 2.1 Master | `fal-ai/kling-video/v2.1/master/text-to-video` | 5s/10s |
| Rẻ nhất | Hailuo 02 | `fal-ai/minimax/hailuo-02/standard/text-to-video` | 6s/10s |

Sora 2 (`sora-2`, OpenAI): vật lý tốt nhưng **API bị khai tử 24/09/2026** — chỉ là fallback cuối.

## Ảnh (qua fal.ai — `FAL_KEY`)

| Nhu cầu | Model | Endpoint | Ghi chú |
|---|---|---|---|
| **Mặc định — photorealism** | FLUX.2 Pro | `fal-ai/flux-2-pro` | dẫn đầu độ chân thực 2026 |
| Dự phòng chất lượng cao | FLUX 1.1 Pro Ultra | `fal-ai/flux-pro/v1.1-ultra` | 2K, rất ổn định |
| Chân thực như ảnh chụp | Imagen 4 | `fal-ai/imagen4/preview` | da/vải/ánh sáng tốt nhất, render chữ tốt |
| Rẻ, nhanh | FLUX dev | `fal-ai/flux/dev` | ~$0.025/ảnh |
| Typography/chữ trong ảnh | Ideogram v3 | `fal-ai/ideogram/v3` | truyền qua `--model` |
| Vector/logo | Recraft v3 | `fal-ai/recraft/v3/text-to-image` | truyền qua `--model` |

## Provider dự phòng (không có FAL_KEY)

| Provider | Ảnh | Video |
|---|---|---|
| `GEMINI_API_KEY` | Imagen 4 (`imagen-4.0-generate-001`) | Veo 3.1 (`veo-3.1-generate-preview`) |
| `OPENAI_API_KEY` | GPT Image (`gpt-image-1`) — đứng đầu arena 2026, mạnh về layout/chữ/đa ràng buộc | Sora 2 (sunset 09/2026) |

## Quy tắc chọn nhanh
- Người dùng không nói gì đặc biệt → cứ để chuỗi mặc định chạy.
- "thật như ảnh chụp" → `--model fal-ai/imagen4/preview`
- ảnh có chữ/poster/banner → `--model fal-ai/ideogram/v3` (hoặc GPT Image nếu chỉ có OpenAI key)
- logo/icon vector → `--model fal-ai/recraft/v3/text-to-image`
- "rẻ/nhanh/thử nháp" → `--model fal-ai/flux/dev` (ảnh), `--model fal-ai/minimax/hailuo-02/standard/text-to-video` (video)
- video dọc TikTok → thêm `--ar 9:16`
