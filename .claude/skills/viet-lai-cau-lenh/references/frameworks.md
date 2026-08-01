# 9 Framework Viết Câu Lệnh — công thức, ví dụ, cách triển khai

Mỗi framework có: **khi nào dùng → template điền → ví dụ → cách triển khai → lỗi thường gặp**.
Thứ tự các chữ cái là bắt buộc: đó chính là thứ tự Claude đọc và suy nghĩ.

---

## 1. R.A.C.E — Công thức khởi đầu

Công thức đầu tiên nên học. Đơn giản nhưng cực kỳ hiệu quả.

- **R — Role**: Claude cần đóng vai gì
- **A — Action**: Nhiệm vụ cần thực hiện
- **C — Context**: Bối cảnh và thông tin chi tiết
- **E — Expectation**: Kết quả cuối cùng mong muốn

**Template**
```
Đóng vai <vai trò + số năm kinh nghiệm>.
Hãy <hành động cụ thể>.
Bối cảnh: <sản phẩm/khách hàng/dữ liệu/ràng buộc>.
Kết quả mong muốn: <số lượng + định dạng + giọng văn + độ dài>.
```

**Ví dụ**
> Đóng vai một chuyên gia marketing strategist.
> Hãy tạo chuỗi email ra mắt sản phẩm dành cho những người bận rộn.
> Tôi sắp bán một sản phẩm số giá 47 USD về productivity.
> Viết chuỗi gồm 5 email tập trung vào tăng tương tác và chuyển đổi.
> Mỗi email dưới 200 từ và có cảm giác như một người bạn đang viết chứ không phải thương hiệu.

**Cách triển khai**: viết R và A trước (một câu mỗi phần), rồi dồn mọi dữ kiện bạn có vào C —
C càng dày, kết quả càng ít chung chung. E phải kiểm chứng được: đếm được hoặc nhìn là biết đạt/không đạt.

**Lỗi thường gặp**: bỏ E → nhận về một bài viết dài lê thê không dùng được.

---

## 2. R.I.S.E — Công thức giải quyết vấn đề

Dùng khi có một vấn đề cụ thể cần phân tích và xử lý.

- **R — Role**: Chuyên môn của Claude
- **I — Identify**: Xác định vấn đề chính
- **S — Steps**: Quy trình Claude cần thực hiện
- **E — Expectation**: Kết quả mong muốn

**Template**
```
Bạn là <chuyên gia lĩnh vực> với <N> năm kinh nghiệm.
Vấn đề hiện tại là <mô tả + số liệu + khoảng thời gian>.
Đầu tiên hãy <phân tích/chẩn đoán>. Sau đó <đề xuất N giải pháp, xếp theo ...>.
Cuối cùng tạo <đầu ra cuối> có thể triển khai trong <thời hạn> để thấy kết quả trong <thời hạn>.
```

**Ví dụ**
> Bạn là chuyên gia tối ưu năng suất cho đội nhóm remote với 15 năm kinh nghiệm.
> Vấn đề hiện tại là tỷ lệ tham gia các buổi họp hàng tuần của team đã giảm 40% trong 2 tháng qua.
> Đầu tiên hãy phân tích nguyên nhân gốc rễ.
> Sau đó đề xuất 5 giải pháp cụ thể theo thứ tự tác động mạnh nhất.
> Cuối cùng tạo một action plan có thể triển khai ngay trong tuần này để thấy kết quả trong vòng 14 ngày.

**Cách triển khai**: S phải là các bước **tuần tự có đánh số** ("Đầu tiên… Sau đó… Cuối cùng…").
Chính chuỗi này buộc Claude suy nghĩ như consultant thực thụ: **chẩn đoán trước, giải pháp sau**.

**Lỗi thường gặp**: gộp I và S làm một → Claude nhảy thẳng vào giải pháp mà chưa tìm nguyên nhân.

---

## 3. S.T.A.R — Framework tập trung vào kết quả

Dùng khi muốn chuyển từ "tình huống hiện tại" sang "kết quả đo lường cụ thể".

- **S — Situation**: Tình huống hiện tại
- **T — Task**: Mục tiêu hoặc thử thách
- **A — Action**: Những việc cần thực hiện
- **R — Result**: Kết quả cụ thể mong muốn đạt được

**Template**
```
Hiện tại <tình huống + chỉ số hiện tại>.
Mục tiêu là <chỉ số mục tiêu> mà không cần <ràng buộc>.
Hãy <phân tích ...>, xác định <N> điểm nghẽn lớn nhất và xây dựng <hệ thống/quy trình mới>.
Mục tiêu cuối cùng là <% thay đổi> trong vòng <thời hạn>.
```

**Ví dụ**
> Hiện tại đội customer support của chúng tôi mất trung bình 24 giờ để phản hồi ticket hỗ trợ.
> Mục tiêu là giảm xuống dưới 4 giờ mà không cần tuyển thêm nhân sự.
> Hãy phân tích workflow hiện tại, xác định 3 bottleneck lớn nhất và xây dựng một hệ thống mới
> sử dụng automation cùng quy trình phân loại ticket hiệu quả hơn.
> Mục tiêu cuối cùng là giảm 60% thời gian phản hồi trong vòng 30 ngày.

**Cách triển khai**: S và R phải là **hai con số cùng đơn vị** (24 giờ → 4 giờ). Có cặp số đó,
Claude tự biết khoảng cách cần lấp và ngừng đưa lời khuyên chung chung.

**Lỗi thường gặp**: R viết kiểu "cải thiện đáng kể" → không đo được, kết quả vô dụng.

---

## 4. S.O.A.P — Framework xây dựng chiến lược

Dùng khi cần xây dựng một chiến lược hoàn chỉnh từ đầu.

- **S — Subject**: Chủ đề chính
- **O — Objective**: Mục tiêu cần đạt
- **A — Action**: Các bước cần thực hiện
- **P — Plan**: Kế hoạch chiến lược cuối cùng

**Template**
```
Chủ đề là <vấn đề/lĩnh vực>.
Mục tiêu là <trạng thái mong muốn> thay vì <trạng thái hiện tại>.
Hãy <phân tích điểm đứt gãy / khảo sát hiện trạng>.
Tạo <kế hoạch + mốc thời gian + checklist theo ngày/tuần>.
```

**Ví dụ**
> Chủ đề là tình trạng onboarding nhân sự bị chậm trễ.
> Mục tiêu là giúp nhân sự mới có thể làm việc hiệu quả ngay trong tuần đầu tiên thay vì mất 3 tuần như hiện tại.
> Hãy phân tích điểm đứt gãy trong quy trình hiện tại và tạo một hệ thống onboarding tối ưu hơn
> kèm checklist công việc cho từng ngày trong 7 ngày đầu tiên.

**Cách triển khai**: khác RISE ở chỗ SOAP kết bằng **P — một bản kế hoạch giao được**, nên
luôn chốt P bằng định dạng cụ thể: checklist theo ngày, bảng RACI, lộ trình 30/60/90.

**Lỗi thường gặp**: để A và P giống nhau → nhận về danh sách việc rời rạc, không thành chiến lược.

---

## 5. C.L.E.A.R — Framework nghiên cứu và tối ưu

Dùng khi đang nghiên cứu, so sánh phương án, hoặc chạy thử nghiệm để tối ưu dần.

- **C — Context**: Bối cảnh, dữ liệu, những gì đã thử
- **L — Limitations**: Giới hạn — ngân sách, thời gian, nhân lực, những thứ không được đụng tới
- **E — Examples**: Ví dụ mẫu hoặc tiêu chí của một kết quả tốt
- **A — Analysis**: Phân tích, so sánh các phương án theo tiêu chí
- **R — Refine**: Vòng tinh chỉnh — chọn phương án tốt nhất và nói rõ cách đo

**Template**
```
Bối cảnh: <dữ liệu hiện có + những gì đã thử và kết quả>.
Giới hạn: <ngân sách / thời gian / công cụ / điều không được thay đổi>.
Kết quả tốt trông như thế này: <ví dụ mẫu hoặc tiêu chí>.
Hãy so sánh <N> phương án theo <các tiêu chí>, trình bày dạng bảng có chấm điểm.
Sau đó chọn phương án tốt nhất, nêu cách đo kết quả và <N> thử nghiệm tiếp theo nếu thất bại.
```

**Ví dụ**
> Bối cảnh: landing page của tôi có 3.000 lượt truy cập/tháng, tỷ lệ chuyển đổi 1,1%; đã thử đổi
> nút CTA sang màu đỏ nhưng không thay đổi gì.
> Giới hạn: ngân sách quảng cáo 5 triệu/tháng, không đổi được nền tảng website, chỉ có 1 người làm.
> Kết quả tốt là một trang đạt trên 3% chuyển đổi, giọng văn giữ nguyên như hiện tại.
> Hãy so sánh 5 phương án tối ưu theo tiêu chí: tác động, công sức, rủi ro — trình bày bảng chấm điểm 1–10.
> Sau đó chọn phương án tốt nhất, nêu chỉ số cần theo dõi và 3 thử nghiệm A/B kế tiếp nếu phương án đầu thất bại.

**Cách triển khai**: **L là phần tạo ra khác biệt** — không nêu giới hạn, Claude sẽ đề xuất
những thứ bạn không có nguồn lực làm. R biến prompt thành vòng lặp: chạy → đo → quay lại
sửa đúng phần yếu, giữ nguyên phần đã tốt.

**Lỗi thường gặp**: chỉ hỏi "làm sao tối ưu?" mà không nói **đã thử gì rồi** → nhận lại đúng những
thứ đã thất bại.

---

## 6. P.A.S.T.O.R — Công thức bán hàng cực mạnh

Cực kỳ hiệu quả cho mọi thứ liên quan bán hàng: email, landing page, DM, quảng cáo.

- **P — Problem**: Nêu vấn đề
- **A — Amplify**: Khuếch đại hậu quả nếu không giải quyết
- **S — Story**: Kể ví dụ thực tế hoặc tình huống dễ đồng cảm
- **T — Transformation**: Cho thấy sự thay đổi trước và sau
- **O — Offer**: Đưa ra giải pháp
- **R — Response**: Kêu gọi hành động tiếp theo

**Template**
```
Bạn là một sales copywriter hàng đầu.
Vấn đề là <nỗi đau của khách hàng + hệ quả kinh doanh>.
Hãy khuếch đại vấn đề bằng cách cho thấy <chi phí của việc không hành động>.
Chia sẻ <case study/tình huống> trong đó <kết quả có số liệu>.
Mô tả quá trình chuyển đổi từ <trạng thái cũ> thành <trạng thái mới>.
Sau đó giới thiệu giải pháp của tôi là <sản phẩm/dịch vụ>.
Kết thúc bằng CTA rõ ràng để <hành động> trong vòng <thời hạn>.
```

**Ví dụ**
> Bạn là một sales copywriter hàng đầu.
> Vấn đề là khách hàng của tôi mua lại quá thấp khiến lifetime revenue giảm mạnh.
> Hãy khuếch đại vấn đề bằng cách cho thấy chi phí của việc mất khách hàng so với giữ chân họ.
> Chia sẻ một case study trong đó loyalty campaign giúp tăng retention lên 25%.
> Mô tả quá trình chuyển đổi từ người mua một lần thành khách hàng trung thành.
> Sau đó giới thiệu giải pháp của tôi là chuỗi email follow-up được cá nhân hóa.
> Kết thúc bằng CTA rõ ràng để triển khai trong vòng 2 tuần.

**Cách triển khai**: giữ đúng thứ tự 6 chữ — đây là thứ tự tâm lý của người mua. Viết A bằng
**con số thiệt hại**, không bằng tính từ. Nêu rõ kênh (email/landing/DM) và độ dài để văn phong khớp kênh.

**Lỗi thường gặp**: nhảy thẳng từ P sang O → thành quảng cáo, mất phần thuyết phục.

---

## 7. F.A.B — Framework giới thiệu sản phẩm

Dùng khi cần giải thích vì sao một thứ thực sự quan trọng.

- **F — Features**: Tính năng
- **A — Advantages**: Lợi thế mà tính năng đó mang lại
- **B — Benefits**: Kết quả thực tế người dùng nhận được

**Template**
```
Bạn là chuyên gia product marketing.
Sản phẩm của tôi có <tính năng>.
Hãy giải thích: tính năng là gì / vì sao tốt hơn <cách làm cũ> / lợi ích thực tế là <kết quả kinh doanh>.
Viết dưới dạng <định dạng + độ dài + nơi sử dụng>.
```

**Ví dụ**
> Bạn là chuyên gia product marketing.
> Công cụ của tôi có dashboard analytics theo thời gian thực.
> Hãy giải thích: tính năng của sản phẩm; vì sao nó tốt hơn cách report thủ công;
> lợi ích thực tế là ra quyết định nhanh hơn, giảm lãng phí thời gian và tăng doanh thu.
> Viết toàn bộ dưới dạng một đoạn pitch 3 dòng cho landing page.

**Cách triển khai**: luôn kết ở **B** bằng ngôn ngữ của khách hàng (tiền, thời gian, sự an tâm),
không phải ngôn ngữ kỹ thuật. Chốt bằng nơi dùng (landing page, slide, tin nhắn bán hàng) để
Claude chỉnh độ dài đúng chỗ đó.

**Lỗi thường gặp**: liệt kê tính năng rồi dừng → khách đọc xong không biết được lợi gì.

---

## 8. 5W1H — Framework nhìn toàn cảnh vấn đề

Dùng khi cần hiểu toàn bộ một tình huống từ mọi góc độ.

- **Who** — Ai liên quan
- **What** — Điều gì đang xảy ra
- **When** — Xảy ra khi nào
- **Where** — Xảy ra ở đâu
- **Why** — Vì sao vấn đề quan trọng
- **How** — Cách giải quyết

**Template**
```
<Mô tả tình huống + thời điểm bắt đầu + nơi xảy ra + chỉ số đang xấu đi>.
Hãy phân tích: ai bị ảnh hưởng / điều gì gây ra / khi nào bắt đầu / bottleneck nằm ở đâu /
vì sao ngày càng nghiêm trọng / cách xử lý bằng <giải pháp> trong vòng <thời hạn>.
```

**Ví dụ**
> Đội support của tôi đang gặp tình trạng backlog ticket tăng mạnh sau bản cập nhật sản phẩm mới nhất.
> Các vấn đề xuất hiện trong hệ thống chat trực tiếp trong ứng dụng.
> Điểm hài lòng của khách hàng đang giảm mỗi ngày.
> Hãy phân tích: ai bị ảnh hưởng; điều gì gây ra backlog; khi nào vấn đề bắt đầu; bottleneck nằm ở đâu;
> vì sao nó ngày càng nghiêm trọng; cách xử lý bằng automation và bổ sung nhân sự hỗ trợ trong vòng 5 ngày làm việc.

**Cách triển khai**: yêu cầu trả lời **theo đúng 6 mục có tiêu đề** để không mục nào bị bỏ sót.
Dùng 5W1H làm bước chẩn đoán, rồi đưa kết quả sang RISE hoặc GROW để ra hành động.

**Lỗi thường gặp**: dừng ở How chung chung → luôn gắn How với thời hạn và nguồn lực cụ thể.

---

## 9. G.R.O.W — Framework đạt mục tiêu

Dùng khi đã có mục tiêu rõ ràng nhưng cần lộ trình cụ thể để đạt được.

- **G — Goal**: Xác định mục tiêu
- **R — Reality**: Thực trạng hiện tại
- **O — Options**: Các lựa chọn hoặc giải pháp khả thi
- **W — Will**: Hành động cụ thể và cam kết thực hiện

**Template**
```
Bạn là <chuyên gia lĩnh vực>.
Mục tiêu của tôi là <mục tiêu + % + thời hạn>.
Hiện tại: <2–4 chỉ số thực tế>.
Hãy đưa ra <N> giải pháp thực tế, bao gồm <gợi ý hướng>.
Sau đó chọn <M> giải pháp tốt nhất và xây dựng action plan theo từng tuần cho <N> tuần tiếp theo,
với công việc cụ thể và deadline rõ ràng.
```

**Ví dụ**
> Bạn là một growth marketing strategist.
> Mục tiêu của tôi là tăng số lượng đăng ký webinar thêm 300% trong vòng 30 ngày tới.
> Hiện tại: tỷ lệ click email là 1,2%; mỗi webinar chỉ có khoảng 50 người đăng ký.
> Hãy đưa ra 5 giải pháp thực tế để đạt mục tiêu, bao gồm: tối ưu subject line; hợp tác với đối tác;
> tạo referral system; test landing page mới; xây dựng email sequence mới.
> Sau đó chọn ra 3 giải pháp tốt nhất và xây dựng action plan theo từng tuần cho 4 tuần tiếp theo,
> với công việc cụ thể và deadline rõ ràng.

**Cách triển khai**: đây là framework các coach dùng để tạo chuyển đổi. Bí quyết là **R phải trung
thực bằng số** — mục tiêu 300% chỉ có nghĩa khi Claude biết điểm xuất phát. W luôn kết bằng
lịch theo tuần, không phải danh sách ý tưởng.

**Lỗi thường gặp**: bỏ O, đi thẳng từ G sang W → chỉ nhận được một phương án, không có lựa chọn thay thế.

---

## Ghi chú về CLEAR
Tài liệu gốc gọi tên CLEAR (framework nghiên cứu và tối ưu) nhưng không tách nghĩa từng chữ cái.
Bản diễn giải ở mục 5 — **Context, Limitations, Examples, Analysis, Refine** — là cách triển khai
được dùng thống nhất trong skill này. Nếu bạn có phiên bản CLEAR khác, sửa mục 5 là toàn bộ
skill chạy theo.
