---
name: viet-lai-cau-lenh
description: >
  Viết lại câu lệnh (prompt) của người dùng theo đúng framework mạnh nhất — RACE, RISE, STAR,
  SOAP, CLEAR, PASTOR, FAB, 5W1H, GROW — kèm hướng dẫn cách triển khai framework đó.
  Use when the user asks to improve/rewrite/optimize a prompt, asks which prompt framework to
  use, or pastes a vague request and wants a better version — in Vietnamese or English
  (viết lại câu lệnh, tối ưu prompt, prompt sao cho hiệu quả, chọn framework, rewrite my prompt,
  improve this prompt, which framework should I use).
---

# Viết Lại Câu Lệnh Theo Framework

Nhận MỘT mô tả nhu cầu (dù mơ hồ) → chọn framework phù hợp nhất → viết lại thành câu lệnh
hoàn chỉnh → **kèm cách triển khai framework** để người dùng tự dùng lại được lần sau.

Không hỏi lại người dùng nếu có thể suy ra hợp lý. Thiếu dữ kiện thì **tự điền giả định**
và đánh dấu rõ bằng `[giả định: ...]` để người dùng sửa — đừng bắt họ điền form.

## Quy trình

### Bước 1 — Đọc nhu cầu, xác định ý định
Tìm trong mô tả của người dùng: họ đang **bắt đầu mới**, **chữa một vấn đề**, **đuổi theo một
con số**, **dựng chiến lược**, **nghiên cứu/thử nghiệm**, **bán hàng**, **giới thiệu sản phẩm**,
**cần nhìn toàn cảnh**, hay **đang có mục tiêu cần lộ trình**.

### Bước 2 — Chọn framework
Dùng bảng quyết định (chi tiết trong `references/frameworks.md`):

| Tình huống | Framework |
|---|---|
| Bắt đầu thứ gì mới | **RACE** |
| Đang giải quyết vấn đề | **RISE** |
| Cần kết quả đo lường cụ thể | **STAR** |
| Đang xây dựng chiến lược | **SOAP** |
| Đang nghiên cứu và test | **CLEAR** |
| Viết nội dung để bán hàng | **PASTOR** |
| Pitch sản phẩm / tính năng | **FAB** |
| Cần phân tích toàn bộ tình huống | **5W1H** |
| Đang theo đuổi một mục tiêu cụ thể | **GROW** |

Chọn đúng **một** framework chính. Nếu nhu cầu bắc cầu hai loại (ví dụ: phân tích rồi mới bán),
chọn framework chính theo *kết quả cuối cùng người dùng cần*, và ghép framework phụ ở phần
"Nâng cấp" (xem `references/trien-khai.md`).

### Bước 3 — Viết lại câu lệnh
Đọc `references/frameworks.md`, lấy đúng template của framework đã chọn rồi điền:
- Viết bằng **ngôn ngữ người dùng đang dùng** (mặc định tiếng Việt).
- Mỗi chữ cái của framework = ít nhất một câu đầy đủ, đúng thứ tự chữ cái.
- Luôn có **con số cụ thể**: số lượng, thời hạn, độ dài, ngưỡng đo lường. Không có số thì tự đề xuất.
- Luôn kết bằng **định dạng đầu ra mong muốn** (bảng, checklist, số từ, giọng văn).
- Câu lệnh mới phải copy-paste chạy được ngay, không chứa chỗ trống bắt buộc điền.

### Bước 4 — Kèm cách triển khai framework (BẮT BUỘC — đừng bỏ)
Đọc `references/trien-khai.md` và xuất thêm:
1. **Bảng ánh xạ**: từng chữ cái → nội dung đã điền trong câu lệnh mới (để họ thấy công thức chạy thế nào).
2. **3 bước triển khai**: dán → chạy → tinh chỉnh, kèm câu lệnh tinh chỉnh mẫu.
3. **Nâng cấp**: 1–2 cách ghép thêm framework khác hoặc siết yêu cầu khi kết quả chưa đủ sâu.

### Bước 5 — Trả kết quả theo đúng bố cục này

```
🎯 Framework: <TÊN> — <một dòng vì sao hợp>

📋 Câu lệnh đã viết lại
<khối copy-paste, không kèm bình luận>

🧩 Cách triển khai framework
<bảng chữ cái → nội dung>
<3 bước: dán / chạy / tinh chỉnh>
<nâng cấp khi cần sâu hơn>
```

Giữ phần giải thích ngắn. Giá trị nằm ở câu lệnh mới, không nằm ở lời dẫn.

## Khi người dùng hỏi "nên dùng framework nào?"
Trả lời bằng framework được chọn + lý do một dòng, rồi **vẫn viết lại luôn câu lệnh** cho họ.
Đừng dừng ở lời khuyên.

## Khi người dùng đưa nhiều nhu cầu một lúc
Tách thành từng câu lệnh riêng, mỗi cái một framework. Không nhồi ba mục tiêu vào một prompt —
đó chính là lý do kết quả bị chung chung.
