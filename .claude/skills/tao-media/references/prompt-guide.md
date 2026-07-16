# Công thức nâng cấp prompt (idea → cinematic prompt)

Prompt cuối cùng LUÔN bằng tiếng Anh (model hiểu tiếng Anh tốt nhất), 60–150 từ cho ảnh,
80–200 từ cho video. Giữ nguyên ý gốc; chỉ thêm chi tiết, không đổi chủ đề.

## Ảnh — công thức 8 lớp

```
[SUBJECT chi tiết] + [ACTION/pose] + [ENVIRONMENT] + [LIGHTING] +
[CAMERA & LENS] + [COMPOSITION] + [STYLE/medium] + [MOOD + chất liệu bề mặt]
```

Ví dụ nâng cấp:
- Ý tưởng: "một chú rồng trên vịnh Hạ Long"
- Prompt: "A majestic golden dragon with iridescent scales soaring low over the emerald
  waters of Ha Long Bay at sunset, limestone karsts silhouetted in layered mist, warm
  golden-hour rim lighting with soft volumetric rays, shot on a cinematic 85mm lens at
  f/2.8, low-angle composition with the dragon dominating the upper third, hyperrealistic
  digital painting in the style of epic fantasy concept art, awe-inspiring mood, water
  spray and scale reflections rendered in intricate detail"

Từ khóa chất lượng theo thể loại:
- **Photorealism**: shot on [máy ảnh], 85mm/35mm lens, f/1.8, natural skin texture,
  subsurface scattering, sharp focus, 8k detail
- **Ánh sáng**: golden hour, blue hour, volumetric light, rim light, chiaroscuro,
  soft diffused studio lighting, neon glow, candlelight
- **Poster/logo/typography**: chữ hiển thị đặt trong ngoặc kép + `bold clean typography,
  vector style, flat design` (ưu tiên model Ideogram/GPT Image cho chữ)
- **Sản phẩm**: studio product photography, seamless white/gradient background,
  softbox lighting, high-gloss reflections

## Video — công thức 9 lớp (Veo 3.1 / Kling)

```
[SHOT TYPE] + [SUBJECT] + [ACTION theo trình tự thời gian] + [ENVIRONMENT] +
[CAMERA MOVEMENT] + [LIGHTING] + [STYLE] + [MOOD/pacing] + [AUDIO]
```

- **Camera movement**: slow dolly-in, sweeping aerial drone shot, handheld tracking,
  orbit shot, crane up, whip pan, static locked-off shot
- **Audio (Veo 3.1 tạo âm thanh đồng bộ)**: mô tả rõ — "sound of waves crashing,
  distant seagulls, a low cinematic score swelling"; hội thoại đặt trong ngoặc kép
  kèm ngôn ngữ: `The fisherman says in Vietnamese: "Đẹp quá!"`
- **Vật lý & liên tục**: mô tả hành động theo thứ tự (first... then... finally...)
  giúp model giữ mạch chuyển động.

Ví dụ nâng cấp:
- Ý tưởng: "video quảng cáo cà phê sữa đá"
- Prompt: "Cinematic close-up commercial shot: condensation beads rolling down a tall
  glass of Vietnamese iced milk coffee on a rustic wooden table, dark espresso slowly
  cascading over ice cubes and swirling into silky condensed milk in mesmerizing clouds,
  soft morning window light with warm bokeh of a Hanoi street cafe in the background,
  slow dolly-in with shallow depth of field, rich amber and cream color palette,
  luxurious and refreshing mood, audio: gentle ice clinks, coffee pouring, soft
  acoustic guitar, ambient street chatter"

## Chọn aspect ratio
| Nội dung | AR |
|---|---|
| Cinematic, phong cảnh, YouTube | 16:9 |
| TikTok/Reels/Shorts, chân dung đứng | 9:16 |
| Logo, avatar, icon | 1:1 |
| Poster, bìa sách | 3:4 |
| Ảnh chân dung nghệ thuật | 3:4 hoặc 9:16 |

## Những lỗi cần tránh
- Đừng nhồi mâu thuẫn (vd. "minimalist" + "intricate details" cho cùng một chủ thể).
- Đừng liệt kê > 3 chủ thể chính — model loãng focus.
- Video: một shot ≤ 8s chỉ nên có MỘT hành động chính + một chuyển máy.
- Negative concepts: diễn đạt xuôi ("empty street") thay vì phủ định ("no people").
