# 🎬 tao-media — Gõ một ý tưởng, ra ngay ảnh & video đẳng cấp

Skill cho Claude Code: biến **một câu ý tưởng** (tiếng Việt hoặc tiếng Anh) thành hình ảnh
hoặc video chất lượng điện ảnh, hoàn toàn tự động — Claude tự nâng cấp prompt theo công thức
chuyên nghiệp, tự chọn model đỉnh nhất, tự tạo và gửi file cho bạn.

## Dùng như thế nào

Trong Claude Code (repo này), chỉ cần gõ:

```
/tao-media một chú rồng vàng bay qua vịnh Hạ Long lúc hoàng hôn
```

hoặc nói tự nhiên:

```
tạo cho tôi video quảng cáo cà phê sữa đá kiểu điện ảnh
vẽ logo cho quán phở tên "Phở Rồng"
```

Claude sẽ: phân loại ảnh/video → viết prompt điện ảnh tiếng Anh (ánh sáng, ống kính,
bố cục, âm thanh…) → gọi model tốt nhất → trả file về ngay trong chat.

### ✨ Perfect Mode (mặc định)

Không chỉ tạo một lần: Claude **tự mở ảnh xem lại, chấm điểm theo rubric 10 tiêu chí**
(đúng ý, giải phẫu, chữ, bố cục, ánh sáng, artifact…), rồi **tự sửa prompt và tạo lại**
cho đến khi đạt ≥ 9/10 (tối đa 3 vòng). Video "đẹp nhất" dùng pipeline chuyên nghiệp:
tạo keyframe ảnh hoàn hảo trước → animate bằng Veo 3.1/Kling **image-to-video** —
bạn chỉ gõ một câu, phần còn lại tự động đến phiên bản hoàn hảo nhất.

## Cài đặt (1 phút — chỉ cần 1 API key)

Chọn MỘT trong ba (ưu tiên theo thứ tự):

| Provider | Lấy key ở đâu | Được gì |
|---|---|---|
| **fal.ai** (khuyên dùng) | https://fal.ai/dashboard/keys | Veo 3.1, Kling 3.0, FLUX.2, Imagen 4, Ideogram… (600+ model) |
| Google AI Studio | https://aistudio.google.com/apikey | Imagen 4 + Veo 3.1 |
| OpenAI | https://platform.openai.com/api-keys | GPT Image (ảnh đứng đầu arena 2026) |

```bash
export FAL_KEY="your-key"          # hoặc
export GEMINI_API_KEY="your-key"   # hoặc
export OPENAI_API_KEY="your-key"
```

Không cần `pip install` gì cả — script chạy bằng Python 3 thuần.

## Model được dùng (nghiên cứu 07/2026)

- **Video**: Veo 3.1 (mặc định — 4K, âm thanh đồng bộ) → Kling 3.0 Pro → Kling 2.1 → Hailuo 02
- **Ảnh**: FLUX.2 Pro (mặc định — photorealism số 1) → FLUX 1.1 Ultra → Imagen 4 → FLUX dev
- Chuyên biệt: Ideogram v3 (chữ trong ảnh), Recraft v3 (logo/vector), GPT Image (layout phức tạp)
- Script tự fallback nếu một model lỗi; Sora 2 không dùng làm mặc định vì OpenAI khai tử API 09/2026.

## Cấu trúc

```
.claude/skills/tao-media/
├── SKILL.md                  # quy trình Claude thực hiện (Perfect Mode)
├── scripts/generate.py       # generator đa provider (fal.ai / Gemini / OpenAI), stdlib thuần
│                             # text-to-image, text-to-video, image-to-video, seed, negative
└── references/
    ├── prompt-guide.md       # công thức prompt điện ảnh 8-9 lớp
    ├── models.md             # bảng định tuyến model + giá
    └── refine-checklist.md   # rubric 10 điểm + bảng sửa lỗi cho vòng lặp hoàn hảo
```

Kết quả lưu tại `media-output/` (tự tạo).

## Dùng script trực tiếp (không qua Claude)

```bash
python3 .claude/skills/tao-media/scripts/generate.py \
  "A majestic golden dragon soaring over Ha Long Bay at sunset..." \
  --type video --ar 16:9 --duration 8 --resolution 1080p
```
