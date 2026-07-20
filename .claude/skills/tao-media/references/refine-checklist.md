# Rubric tự chấm & vòng lặp hoàn hảo (Perfect Mode)

Sau mỗi lần tạo ảnh, Claude PHẢI mở file ảnh bằng tool Read (Read xem được ảnh),
chấm theo 10 tiêu chí dưới đây (mỗi tiêu chí 1 điểm), rồi quyết định tạo lại hay giao hàng.

## Rubric 10 điểm

| # | Tiêu chí | Đạt khi |
|---|---|---|
| 1 | Đúng ý tưởng | Chủ thể + bối cảnh khớp ý gốc của người dùng |
| 2 | Chủ thể sắc nét | Không mờ, không biến dạng, đủ chi tiết |
| 3 | Giải phẫu/cấu trúc | Tay, mặt, chân tay, kiến trúc, logic vật thể đúng |
| 4 | Chữ (nếu có) | Đúng chính tả từng ký tự, không chữ rác |
| 5 | Bố cục | Cân bằng, chủ thể đặt đúng, không cắt cụt vô lý |
| 6 | Ánh sáng | Nhất quán hướng sáng, có chiều sâu, không cháy/bệt |
| 7 | Màu sắc | Palette hài hòa, đúng mood yêu cầu |
| 8 | Không artifact | Không vật thể lạ, không lặp pattern, không viền AI |
| 9 | Chất liệu bề mặt | Da/vải/kim loại/nước có texture thật |
| 10 | Cảm xúc tổng thể | Nhìn là "wow", đạt chuẩn dùng được ngay |

**Ngưỡng giao hàng: ≥ 9/10.** Dưới ngưỡng → tinh chỉnh prompt và tạo lại (tối đa 3 vòng).
Hết 3 vòng chưa đạt → giao bản điểm cao nhất và nói rõ điểm còn hạn chế.

## Cách sửa lỗi thường gặp (điền vào prompt vòng sau)

| Lỗi phát hiện | Cách sửa prompt |
|---|---|
| Tay/ngón sai | thêm `anatomically correct hands, five fingers` + đổi pose giấu tay |
| Mặt biến dạng | thêm `detailed symmetrical face, natural expression`; ảnh chân dung → thử `fal-ai/imagen4/preview` |
| Chữ sai chính tả | chuyển `--model fal-ai/ideogram/v3`; đặt chữ trong "..." và rút ngắn chữ |
| Mờ/thiếu nét | thêm `sharp focus, highly detailed, 8k`; bỏ từ gây mờ (dreamy, soft) nếu không cần |
| Bố cục rối | giảm số chủ thể; thêm `rule of thirds composition, clean background` |
| Ánh sáng bẹt | thêm nguồn sáng cụ thể: `dramatic side lighting, volumetric light` |
| Sai style | nêu đích danh medium: `oil painting / 3D render / film photography, Kodak Portra` |
| Vật thể lạ/artifact | mô tả background tường minh + đơn giản hóa cảnh |
| Màu xỉn | thêm `vibrant color grading, cinematic color palette` |
| Đúng hết nhưng nhạt | tăng kịch tính: góc máy thấp/cao, thời tiết, giờ vàng, tương phản |

- Dùng lại `--seed` của bản tốt nhất khi chỉ muốn sửa MỘT lỗi nhỏ (FLUX) — giữ nguyên phần đẹp.
- Mỗi vòng chỉ sửa 1–3 điểm yếu nhất, đừng viết lại prompt từ đầu.

## Video — kiểm tra gián tiếp
Claude không xem được video trực tiếp. Quy trình:
1. Nếu máy có `ffmpeg`: trích 3 frame (`ffmpeg -i video.mp4 -vf "select=eq(n\,0)+eq(n\,90)+eq(n\,180)" -vsync vsync_drop f_%d.png` hoặc `-ss` từng mốc) rồi chấm frame theo rubric trên.
2. Không có ffmpeg: chấm bằng keyframe đầu vào (nếu dùng Perfect Video Pipeline) và giao kèm ghi chú.

## Perfect Video Pipeline (chất lượng đỉnh nhất)
Video đẹp nhất sinh ra từ ảnh đẹp nhất:
1. Tạo keyframe ảnh theo vòng lặp hoàn hảo ở trên (đạt ≥ 9/10).
2. Animate keyframe: `generate.py "MOTION + AUDIO prompt" --type video --image <keyframe.png>`
   (tự route sang Veo 3.1 / Kling image-to-video).
3. Prompt video lúc này CHỈ tả chuyển động + âm thanh, không tả lại cảnh.
