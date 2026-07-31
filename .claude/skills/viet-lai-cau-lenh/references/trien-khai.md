# Cách triển khai framework — phần luôn đi kèm câu lệnh đã viết lại

Câu lệnh mới giải quyết việc hôm nay. Phần triển khai này giúp người dùng **tự viết lại được lần sau**.
Luôn xuất đủ 3 mục dưới đây, ngắn gọn, không giảng giải dài dòng.

---

## Mục 1 — Bảng ánh xạ chữ cái → nội dung đã điền

Cho người dùng thấy công thức đã chạy như thế nào trên chính nhu cầu của họ:

| Chữ cái | Nghĩa | Đã điền gì trong câu lệnh của bạn |
|---|---|---|
| R | Role | Chuyên gia marketing strategist |
| A | Action | Viết chuỗi 5 email ra mắt sản phẩm |
| C | Context | Sản phẩm số 47 USD, đối tượng người bận rộn |
| E | Expectation | Mỗi email < 200 từ, giọng như bạn bè, tối ưu chuyển đổi |

Quy tắc: **một dòng cho mỗi chữ cái**, trích đúng chữ trong câu lệnh mới (không diễn giải lại).
Chỗ nào bạn tự suy ra thì ghi rõ `[giả định]` để người dùng sửa đúng chỗ.

---

## Mục 2 — Ba bước triển khai

Viết đúng ba bước này, có nội dung cụ thể theo từng trường hợp:

1. **Dán** — copy câu lệnh vào Claude, sửa các chỗ `[giả định: ...]` thành số liệu thật của bạn.
   Số liệu thật là thứ tạo ra chênh lệch chất lượng lớn nhất.
2. **Chạy** — gửi nguyên khối, không tách nhỏ. Framework chỉ phát huy khi Claude đọc đủ các chữ cái cùng lúc.
3. **Tinh chỉnh** — chưa ưng thì đừng viết lại từ đầu, chỉ siết **đúng một chữ cái**:
   - Kết quả chung chung → dày thêm **C / Reality / Situation** (thêm số liệu, thêm ràng buộc).
   - Kết quả lan man → siết **E / Result** (giới hạn số từ, số mục, định dạng bảng).
   - Kết quả hời hợt → siết **S / Steps / Options** (bắt phân tích trước, bắt đưa N phương án).
   - Giọng văn sai → sửa **Role** (thêm chuyên môn, thêm "viết cho <đối tượng>").

   Câu tinh chỉnh mẫu:
   > Giữ nguyên cấu trúc trên, chỉ làm lại phần <chữ cái>: <yêu cầu mới>.

---

## Mục 3 — Nâng cấp khi cần sâu hơn

Chọn 1–2 cách hợp với nhu cầu, mỗi cách một dòng:

- **Ghép framework**: chẩn đoán bằng **5W1H** hoặc **RISE**, rồi đưa kết luận sang **GROW/SOAP**
  để ra lộ trình; nghiên cứu bằng **CLEAR** rồi viết bán hàng bằng **PASTOR**.
- **Bắt Claude chấm điểm chính nó**: "Sau khi viết xong, tự chấm kết quả theo <tiêu chí>, chỉ ra
  điểm yếu nhất rồi viết lại bản tốt hơn."
- **Ép chọn phương án**: "Đưa 3 phương án khác hướng nhau, so sánh theo tác động/công sức/rủi ro,
  rồi khuyến nghị một phương án và nói rõ vì sao."
- **Chốt định dạng giao được**: bảng, checklist theo ngày, lịch theo tuần, script gọi điện —
  nói rõ ngay trong câu lệnh thay vì sửa sau.

---

## Lộ trình học 8 bước (dùng khi người dùng hỏi "học cái nào trước?")

| Bước | Framework | Học để làm gì |
|---|---|---|
| 1 | RACE | Công thức khởi đầu — dùng được cho 80% nhu cầu hằng ngày |
| 2 | RISE | Giải quyết vấn đề — buộc chẩn đoán trước, giải pháp sau |
| 3 | STAR | Ra kết quả đo lường được, không phải lời khuyên chung |
| 4 | SOAP + CLEAR | Xây chiến lược hoàn chỉnh; nghiên cứu và tối ưu theo vòng lặp |
| 5 | PASTOR | Viết mọi thứ liên quan bán hàng: email, landing page, DM, quảng cáo |
| 6 | FAB + 5W1H | Pitch sản phẩm; nhìn toàn cảnh một tình huống |
| 7 | GROW | Biến mục tiêu đã có thành lộ trình theo tuần |
| 8 | Chọn đúng framework | Một câu hỏi duy nhất: mình đang ở tình huống nào? |

---

## Bảng chọn nhanh (Bước 8)

Đừng suy nghĩ quá phức tạp. Chỉ cần tự hỏi một câu:

- Đang bắt đầu thứ gì mới? → **RACE**
- Đang giải quyết vấn đề? → **RISE**
- Cần kết quả đo lường cụ thể? → **STAR**
- Đang xây dựng chiến lược? → **SOAP**
- Đang nghiên cứu và test? → **CLEAR**
- Đang viết nội dung để bán hàng? → **PASTOR**
- Đang pitch sản phẩm? → **FAB**
- Cần phân tích toàn bộ tình huống? → **5W1H**
- Đang theo đuổi một mục tiêu cụ thể? → **GROW**

---

## Câu lệnh "tư vấn framework" (đưa cho người dùng khi họ muốn tự chạy ở nơi khác)

```
Bạn là chuyên gia tư vấn prompt formula cho tôi.
Tôi sẽ mô tả điều mình cần hỗ trợ.
Dựa trên mô tả đó, hãy đề xuất framework phù hợp nhất trong các framework sau:
RACE, RISE, STAR, SOAP, CLEAR, PASTOR, FAB, 5W1H, GROW.
Sau đó viết lại yêu cầu của tôi bằng đúng framework đó để tôi nhận được kết quả tốt nhất,
kèm bảng ánh xạ từng chữ cái với nội dung đã điền và cách tinh chỉnh nếu kết quả chưa đạt.
Đây là điều tôi cần:
[MÔ TẢ NHIỆM VỤ CỦA BẠN]
```

Trong repo này thì không cần dán — gõ thẳng `/viet-lai-cau-lenh <nhu cầu của bạn>` là đủ.
