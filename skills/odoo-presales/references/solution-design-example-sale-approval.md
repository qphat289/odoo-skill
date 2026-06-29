# Example Solution Design: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting `Solution Design.docx`.

It shows how to bridge requirement analysis, fit-gap, and functional design into a business-facing solution decision document before technical design starts.

Paired references:

- `skills/odoo-presales/references/requirement-analysis-example-sale-approval.md`
- `skills/odoo-presales/references/fit-gap-analysis-example-sale-approval.md`
- `skills/odoo-presales/references/functional-design-example-sale-approval.md`
- `skills/odoo-module-generation/references/technical-design-example-sale-approval.md`

Example filename: `Solution Design.docx`

---

# Solution Design

## 1. Tóm Tắt Giải Pháp

Giải pháp đề xuất sử dụng Odoo Sales làm nền tảng chuẩn cho quy trình bán hàng, kết hợp cấu hình chính sách bán hàng, custom approval flow cho trường hợp vượt ngưỡng chiết khấu, tích hợp CRM follow-up cho cơ hội đã chốt, và outbound API sync tới hệ thống loyalty.

Định hướng giải pháp:

- ưu tiên tận dụng standard `sale` và `crm`
- dùng configuration cho các ngưỡng, vai trò, và template thông báo khi phù hợp
- chỉ custom ở các điểm standard không bao phủ đủ
- dùng integration tách biệt cho hệ thống loyalty để vận hành và retry rõ ràng

## 2. Mục Tiêu Và Phạm Vi

### 2.1 In Scope

- Quyết định giải pháp cho approval flow đơn bán hàng vượt ngưỡng
- Quyết định giải pháp handoff đơn hàng sang CRM follow-up
- Quyết định giải pháp đồng bộ trạng thái đơn sang loyalty platform

### 2.2 Out Of Scope

- Loyalty point calculation engine
- Dashboard BI nâng cao
- Mobile approval app

### 2.3 Nguyên tắc ra quyết định

- Ưu tiên standard Odoo trước custom
- Chỉ custom khi yêu cầu nghiệp vụ hoặc kiểm soát vận hành không thể đạt bằng configuration
- Tách phần integration thành logic dễ theo dõi lỗi và retry
- Không kéo phase 2 vào phase hiện tại

## 3. Bức Tranh Giải Pháp Tổng Thể

### 3.1 Solution overview

- Sales tạo và quản lý SO trên Odoo
- Approval layer áp trên SO khi discount vượt threshold
- CRM follow-up nhận dữ liệu từ các SO đã đạt điều kiện
- Loyalty platform nhận trạng thái SO qua outbound API

### 3.2 Phân hệ tham gia

- `sale`
- `sale_management`
- `crm`
- `mail`
- hệ thống loyalty bên ngoài

### 3.3 Luồng dữ liệu / vai trò chính

- Sales tạo SO
- Manager xử lý approval
- Odoo đẩy follow-up sang CRM
- Odoo gửi trạng thái đơn sang loyalty
- Key user theo dõi trạng thái approval và sync

## 4. Bản Đồ Giải Pháp Theo Nhóm Yêu Cầu

| Nhóm yêu cầu | Nghiệp vụ | Standard | Configuration | Customization | Integration | Process Change | Ghi chú |
|---|---|---|---|---|---|---|---|
| Approval | Phê duyệt SO vượt ngưỡng | một phần | ngưỡng và vai trò | approval flow trên SO | không | nhẹ | cần chặn confirm khi chưa duyệt |
| CRM follow-up | Chuyển đơn thắng sang CRM | không đủ | mapping tham số | bridge logic | có | không | tránh tạo follow-up trùng |
| Loyalty sync | Đồng bộ trạng thái đơn | không | endpoint và credential | sync log và retry flow | có | không | cần trạng thái Pending / Success / Failed |

## 5. Tóm Tắt Quyết Định Fit/Gap

- `GAP01` Approval flow: Standard chưa đáp ứng đủ logic phê duyệt nhiều cấp theo ngưỡng, cần custom phần kiểm soát confirm và approval state.
- `GAP02` CRM handoff: Standard không có luồng handoff đúng với nhu cầu follow-up sau chốt đơn, cần custom bridge logic.
- `GAP03` Loyalty sync: Standard không có outbound sync và retry tracking cho loyalty platform, cần integration module riêng.

## 6. Phương Án Giải Pháp Được Chọn

### 6.1 Phê duyệt đơn bán hàng

#### 6.1.1 Nhu cầu hiện tại

Đơn bán hàng vượt ngưỡng chiết khấu phải được phê duyệt bởi quản lý trước khi xác nhận.

#### 6.1.2 Phương án được chọn

Mở rộng quy trình SO bằng một approval state nghiệp vụ, chỉ cho phép confirm khi approval đã đạt điều kiện.

#### 6.1.3 Lý do chọn

- giữ người dùng làm việc trên luồng SO quen thuộc
- đảm bảo kiểm soát ngay tại điểm xác nhận đơn
- dễ truy vết trạng thái phê duyệt

#### 6.1.4 Các phương án không chọn

- Dùng quy trình ngoài Odoo qua email thủ công: không đảm bảo traceability
- Tách approval thành hệ thống riêng: tăng phức tạp vận hành

#### 6.1.5 Tác động lên người dùng / quy trình / dữ liệu

- Sales phải chờ duyệt trong trường hợp vượt ngưỡng
- Manager có thêm trách nhiệm approve/reject
- Cần lưu thêm trạng thái và lịch sử approval

### 6.2 Handoff sang CRM follow-up

#### 6.2.1 Nhu cầu hiện tại

Đơn bán hàng đủ điều kiện cần được chuyển sang đội CRM để follow-up sau bán.

#### 6.2.2 Phương án được chọn

Tạo bridge logic từ SO sang record follow-up CRM dựa trên điều kiện nghiệp vụ và mapping customer.

#### 6.2.3 Lý do chọn

- đảm bảo CRM nhận đúng dữ liệu đúng thời điểm
- tránh thao tác tay lặp lại
- cho phép kiểm soát duplicate

#### 6.2.4 Các phương án không chọn

- Cho người dùng tạo follow-up thủ công: rủi ro thiếu hoặc sai dữ liệu
- Đồng bộ toàn bộ SO sang CRM không điều kiện: gây nhiễu vận hành CRM

#### 6.2.5 Tác động lên người dùng / quy trình / dữ liệu

- Key user CRM cần quản lý mapping khách hàng
- Follow-up process được tự động hóa
- Cần hiển thị trạng thái handoff để người dùng theo dõi

### 6.3 Đồng bộ loyalty qua API

#### 6.3.1 Nhu cầu hiện tại

Sau khi SO đạt điều kiện, trạng thái đơn phải được gửi sang loyalty platform để phục vụ tích điểm và chương trình khách hàng thân thiết.

#### 6.3.2 Phương án được chọn

Xây dựng outbound API sync riêng với cơ chế log kết quả và retry có kiểm soát.

#### 6.3.3 Lý do chọn

- tách biệt trách nhiệm integration khỏi quy trình bán hàng chính
- dễ giám sát lỗi
- giảm rủi ro mất dữ liệu đồng bộ

#### 6.3.4 Các phương án không chọn

- Gọi API đồng bộ cứng ngay trong thao tác người dùng mà không có log: khó vận hành khi lỗi
- Đồng bộ batch cuối ngày: không đáp ứng nhu cầu gần real-time

#### 6.3.5 Tác động lên người dùng / quy trình / dữ liệu

- Key user cần theo dõi trạng thái sync
- Cần giữ loyalty ID và response log
- Quy trình xử lý lỗi cần owner rõ ràng

## 7. Tích Hợp Và Luồng Dữ Liệu Tổng Thể

- CRM handoff được kích hoạt sau khi SO thỏa điều kiện nghiệp vụ.
- Loyalty sync được kích hoạt khi SO đạt trạng thái đồng bộ yêu cầu.
- Với cả hai luồng tích hợp, hệ thống cần lưu trạng thái xử lý và thông tin lỗi ở mức nghiệp vụ để key user theo dõi.

## 8. Phân Quyền, Kiểm Soát Và Tuân Thủ

- Sales được tạo và cập nhật SO trong phạm vi quyền hạn.
- Manager được approve/reject các yêu cầu phê duyệt.
- Key user hoặc admin được xem trạng thái sync và xử lý retry theo phân quyền được chốt.
- Các hành động approval và sync failure cần có log tra soát.

## 9. Chuyển Đổi Dữ Liệu Và Cutover

- Chuẩn bị customer mapping cho CRM và loyalty trước UAT.
- Xác nhận danh sách approver theo sales team trước khi training và cutover.
- Đối soát một tập SO mẫu giữa Odoo, CRM, và loyalty trong SIT trước go-live.

## 10. Phân Kỳ Triển Khai

- Phase 1: approval flow, CRM handoff, loyalty sync nền tảng
- Phase 2: dashboard nâng cao, tối ưu cảnh báo, mở rộng automation nếu có

## 11. Rủi Ro, Giả Định, Phụ Thuộc

- Phụ thuộc customer cung cấp mapping CRM và loyalty đầy đủ.
- Phụ thuộc key user xác nhận approval matrix đúng hạn.
- Nếu API loyalty chưa ổn định, tiến độ SIT và UAT có thể bị ảnh hưởng.

## 12. Confirmation Baseline And Applied Assumptions

| ID | Clarification Ref | Confirmed input / applied assumption | Impact on solution | Status |
|---|---|---|---|---|
| SD-CF-01 | `CL-001` | credit block applies when overdue amount exists or credit limit is exceeded | drives approval and validation rules | Confirmed |
| SD-CF-02 | `CL-002` | low-margin case goes through approval path instead of hard block | keeps treatment as process change plus approval | Confirmed |
| SD-CF-03 | `CL-003` | outbound API phase 1 is synchronous only | avoids callback design in current scope | Confirmed |

## 13. Sign-Off / Review Notes

| Vai trò | Đại diện | Trạng thái review | Ghi chú |
|---|---|---|---|
| PM dự án |  | Pending |  |
| FC lead |  | Pending |  |
| Technical lead |  | Pending |  |
| Đại diện khách hàng |  | Pending |  |
