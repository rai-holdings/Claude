# Quy ước cho repo này

## Chế độ viết lại câu lệnh tự động (mặc định BẬT)

Mỗi khi người dùng nhắn một yêu cầu công việc, **tự động** áp dụng skill
`viet-lai-cau-lenh` (`.claude/skills/viet-lai-cau-lenh/SKILL.md`) trước khi bắt tay làm —
người dùng không cần gõ `/viet-lai-cau-lenh`.

Trình tự bắt buộc:

1. Chọn framework phù hợp nhất: RACE, RISE, STAR, SOAP, CLEAR, PASTOR, FAB, 5W1H, GROW.
2. Viết lại yêu cầu thành câu lệnh hoàn chỉnh theo framework đó.
3. In ra đủ 4 phần:

   ```
   🎯 Framework: <TÊN> — <một dòng vì sao hợp>

   📋 Câu lệnh đã viết lại
   <khối copy-paste>

   🧩 Cách triển khai framework
   <bảng chữ cái → nội dung đã điền> + <3 bước dán/chạy/tinh chỉnh> + <cách nâng cấp>

   ⚡ Bổ sung
   <dữ liệu còn thiếu nên cung cấp> + <câu lệnh bước tiếp theo>
   ```

4. **Thực hiện luôn** câu lệnh đã viết lại, không dừng chờ xác nhận. Chỗ nào tự suy ra thì
   đánh dấu `[giả định: ...]` trong câu lệnh để người dùng sửa.

### Khi nào BỎ QUA việc viết lại

Trả lời hoặc làm thẳng, không viết lại, nếu tin nhắn là:

- câu xã giao / phản hồi ngắn: "ok", "đúng rồi", "tiếp tục", "cảm ơn", "dừng lại"
- câu trả lời cho câu hỏi Claude vừa hỏi, hoặc chỉnh sửa nhỏ việc đang làm dở
- lệnh slash (`/tao-media`, `/viet-lai-cau-lenh`, …) — skill tự lo phần của nó
- câu hỏi về chính công việc vừa làm ("sao lại làm vậy?", "sửa file nào?")

### Bật/tắt

- "tắt viết lại" / "khỏi viết lại" / "làm thẳng đi" → ngừng viết lại đến hết phiên
- "bật lại viết lại" → bật lại

Giữ phần viết lại gọn. Giá trị nằm ở kết quả công việc, không nằm ở lời dẫn.
