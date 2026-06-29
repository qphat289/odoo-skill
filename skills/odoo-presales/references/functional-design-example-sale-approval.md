# Example Functional Design: Sale Approval, CRM Handoff, and API Sync

Use this file as a realistic reference when drafting `Functional Design.docx`.

It follows the canonical FSD structure that was extracted from the original sample template, so the agent can generate a full customer-facing FSD without depending on a separate `.docx` template file.

Paired references:

- `skills/odoo-presales/references/requirement-analysis-example-sale-approval.md`
- `skills/odoo-presales/references/fit-gap-analysis-example-sale-approval.md`
- `skills/odoo-module-generation/references/technical-design-example-sale-approval.md`
- `skills/odoo-quality/references/test-plan-example-sale-approval.md`
- `skills/odoo-module-generation/references/project-tracking-example-sale-approval.md`

Example filename: `Functional Design.docx`

---

# Functional Design

## 1. Thông Tin Tổng Quan (Document Control)

### 1.1 Thông tin dự án

- Tên dự án: Triển khai Odoo Sales Governance
- Khách hàng: ABC Trading
- Tên tài liệu: Functional Design - Sale Approval, CRM Handoff, and API Sync
- Phiên bản Odoo mục tiêu: Odoo 17
- Trạng thái tài liệu: Draft
- Người soạn: FC / BA
- Người review: PM, Solution Owner, Key User Sales

### 1.2 Lịch sử thay đổi

| Phiên bản | Ngày | Người thực hiện | Nội dung thay đổi | Trạng thái |
|---|---|---|---|---|
| v0.1 | 2026-06-25 | FC / BA | Khởi tạo tài liệu từ requirement và fit-gap | Draft |
| v0.2 | 2026-06-26 | FC / BA | Bổ sung luồng phê duyệt và handoff CRM | Review |

### 1.3 Tài liệu tham chiếu

- Requirement file từ khách hàng
- `Requirement Analysis.md`
- `Clarification Register.xlsx`
- `Fit-Gap Analysis.xlsx`
- Biên bản workshop Sales và CRM

## 2. Phạm Vi Phân Tích Và Đối Tượng Sử Dụng (Scope & Audience)

### 2.1 In Scope

- Phê duyệt đơn bán hàng vượt ngưỡng chiết khấu
- Handoff cơ hội thắng sang CRM follow-up flow
- Đồng bộ trạng thái đơn bán hàng sang hệ thống loyalty bên ngoài qua API

### 2.2 Out Of Scope

- Loyalty point calculation engine
- Mobile app cho approver
- Dashboard BI nâng cao cho ban giám đốc

### 2.3 Đối tượng sử dụng tài liệu

- FC / BA
- PM
- Dev
- QA/QC
- Sales key user
- Sales manager
- Đại diện khách hàng

## 3. Kiến Trúc Tổng Thể Và Dữ Liệu Master (Architecture & Master Data)

### 3.1 Cấu trúc tổ chức

- Công ty sử dụng một pháp nhân
- Sales team chia theo vùng Bắc / Trung / Nam
- Mỗi vùng có ít nhất một Sales Manager đóng vai trò approver

### 3.2 Master data

- Product master
- Pricelist
- Customer master
- Sales team
- Approval threshold theo vai trò hoặc nhóm khách hàng

### 3.3 Quy ước dữ liệu chính

- Mã đơn bán hàng theo chuẩn SO/YY/MM/Sequence
- Khách hàng phải có mã CRM mapping trước khi handoff
- Trạng thái đồng bộ loyalty dùng tập giá trị: Pending / Success / Failed

## 4. Phân Tích Quy Trình Nghiệp Vụ Chi Tiết (To-Be Business Processes)

### 4.1 Quy trình phê duyệt đơn bán hàng vượt ngưỡng

#### 4.1.1 Mục tiêu quy trình

Đảm bảo đơn bán hàng có chiết khấu vượt ngưỡng không được xác nhận trực tiếp bởi nhân viên sales mà phải đi qua cấp phê duyệt phù hợp.

#### 4.1.2 Sơ đồ quy trình To-Be

- Sales tạo hoặc chỉnh đơn bán hàng
- Hệ thống kiểm tra ngưỡng chiết khấu
- Nếu vượt ngưỡng, hệ thống tạo yêu cầu phê duyệt
- Manager phê duyệt hoặc từ chối
- Nếu được phê duyệt, đơn được phép xác nhận

#### 4.1.3 Bảng bước thực hiện

| Bước | Phòng ban / Vai trò | Hành động trên hệ thống | Kết quả / chứng từ sinh ra |
|---|---|---|---|
| 1 | Sales | Tạo hoặc cập nhật đơn bán hàng | SO ở trạng thái Draft |
| 2 | Odoo | Kiểm tra discount threshold | Xác định có cần approval hay không |
| 3 | Odoo | Tạo approval request khi vượt ngưỡng | Approval request ở trạng thái Waiting |
| 4 | Sales Manager | Xem và quyết định phê duyệt | Approval request Approved hoặc Rejected |
| 5 | Sales | Xác nhận đơn sau khi được duyệt | SO chuyển sang Sale Order |

#### 4.1.4 Business rules

- Nếu mức chiết khấu không vượt ngưỡng, sales được xác nhận đơn trực tiếp.
- Nếu khách hàng thuộc nhóm strategic account, ngưỡng chiết khấu áp dụng theo bảng riêng.
- Một đơn chỉ được xác nhận khi tất cả approval bắt buộc đã hoàn tất.

#### 4.1.5 Exception handling

- Nếu manager từ chối, sales phải điều chỉnh đơn hoặc hủy yêu cầu.
- Nếu approver nghỉ phép, PM hoặc key user xác nhận người thay thế theo phân quyền được cấu hình.

### 4.2 Quy trình handoff sang CRM follow-up

#### 4.2.1 Mục tiêu quy trình

Khi đơn bán hàng thỏa điều kiện, hệ thống cần đẩy thông tin sang CRM để đội chăm sóc khách hàng tiếp tục follow-up hậu bán.

#### 4.2.2 Sơ đồ quy trình To-Be

- SO được xác nhận
- Odoo kiểm tra điều kiện handoff
- Nếu đủ điều kiện, hệ thống tạo hoặc cập nhật follow-up record phía CRM

#### 4.2.3 Bảng bước thực hiện

| Bước | Phòng ban / Vai trò | Hành động trên hệ thống | Kết quả / chứng từ sinh ra |
|---|---|---|---|
| 1 | Sales | Xác nhận SO | SO confirmed |
| 2 | Odoo | Kiểm tra điều kiện handoff | Hệ thống xác định có đẩy CRM hay không |
| 3 | Odoo / CRM | Gửi dữ liệu follow-up | CRM record được tạo hoặc cập nhật |

#### 4.2.4 Business rules

- Chỉ handoff khi khách hàng có CRM mapping hợp lệ.
- Không tạo trùng follow-up cho cùng một SO nếu đã có record active.

#### 4.2.5 Exception handling

- Nếu CRM không phản hồi, trạng thái handoff ghi nhận Failed và cho phép retry.

### 4.3 Quy trình đồng bộ loyalty qua API

#### 4.3.1 Mục tiêu quy trình

Đảm bảo trạng thái đơn bán hàng được gửi sang hệ thống loyalty phục vụ tích điểm và chương trình khách hàng thân thiết.

#### 4.3.2 Sơ đồ quy trình To-Be

- SO confirmed hoặc delivered
- Odoo gửi payload sang loyalty API
- Hệ thống nhận kết quả và ghi log

#### 4.3.3 Bảng bước thực hiện

| Bước | Phòng ban / Vai trò | Hành động trên hệ thống | Kết quả / chứng từ sinh ra |
|---|---|---|---|
| 1 | Odoo | Chuẩn bị payload đồng bộ | Payload sẵn sàng gửi |
| 2 | External System | Nhận request loyalty | Response code và message |
| 3 | Odoo | Cập nhật trạng thái sync | Pending / Success / Failed |

#### 4.3.4 Business rules

- Payload phải chứa mã khách hàng, mã đơn, ngày xác nhận và tổng tiền hợp lệ.
- Không đồng bộ nếu khách hàng chưa có loyalty ID.

#### 4.3.5 Exception handling

- Nếu API timeout, hệ thống ghi log và đưa vào danh sách retry.
- Nếu response validation lỗi, key user phải xử lý dữ liệu master trước khi retry.

## 5. Phân Tích Khoảng Cách Và Giải Pháp (Fit/Gap Summary)

| ID | Yêu cầu khách hàng | Khả năng đáp ứng Standard | Giải pháp đề xuất | Mức độ ưu tiên |
|---|---|---|---|---|
| GAP01 | Phê duyệt nhiều cấp theo ngưỡng discount | Một phần | Customize approval flow | High |
| GAP02 | Handoff follow-up sang CRM | Không có chuẩn phù hợp | Tích hợp / custom handoff logic | High |
| GAP03 | Đồng bộ loyalty qua API và theo dõi retry | Không có chuẩn phù hợp | Integration module + sync log | High |

## 6. Yêu Cầu Chức Năng Chi Tiết (Functional Requirements)

### FR-001 Phê duyệt đơn bán hàng vượt ngưỡng

- Nguồn yêu cầu: RQ-001 / GAP01
- Mục tiêu nghiệp vụ: kiểm soát giảm giá vượt quyền hạn
- Actor / vai trò: Sales, Sales Manager
- Điều kiện đầu vào: SO ở trạng thái Draft
- Luồng chính: hệ thống kiểm tra ngưỡng, tạo approval request, approver xử lý, SO được xác nhận nếu approved
- Luồng ngoại lệ: approver từ chối hoặc không có approver hợp lệ
- Trường dữ liệu liên quan: discount rate, approval status, approver, approval note
- Validation rules: không cho xác nhận nếu approval status chưa đạt yêu cầu
- Kỳ vọng phân quyền: sales tạo request, manager duyệt, admin cấu hình threshold
- Báo cáo / chứng từ liên quan: approval log, sale order form
- Acceptance criteria: đơn vượt ngưỡng không xác nhận được khi chưa được duyệt

### FR-002 Handoff đơn thắng sang CRM follow-up

- Nguồn yêu cầu: RQ-005 / GAP02
- Mục tiêu nghiệp vụ: chuyển giao thông tin khách hàng cho đội chăm sóc
- Actor / vai trò: Sales, CRM team, Odoo
- Điều kiện đầu vào: SO confirmed và có CRM mapping
- Luồng chính: hệ thống gửi dữ liệu sang CRM và ghi nhận kết quả
- Luồng ngoại lệ: CRM lỗi hoặc mapping thiếu
- Trường dữ liệu liên quan: customer, SO number, sales team, handoff status
- Validation rules: không handoff nếu thiếu CRM external ID
- Kỳ vọng phân quyền: key user CRM xem trạng thái handoff
- Báo cáo / chứng từ liên quan: handoff status list
- Acceptance criteria: CRM nhận đúng record và không tạo bản ghi trùng

### FR-003 Đồng bộ loyalty API và theo dõi retry

- Nguồn yêu cầu: RQ-007 / GAP03
- Mục tiêu nghiệp vụ: gửi trạng thái đơn sang loyalty platform
- Actor / vai trò: Odoo, External loyalty system, key user
- Điều kiện đầu vào: SO đủ điều kiện sync
- Luồng chính: tạo payload, gửi API, nhận response, lưu sync status
- Luồng ngoại lệ: timeout, validation error, response lỗi
- Trường dữ liệu liên quan: loyalty ID, sync status, retry count, last response
- Validation rules: không gửi nếu thiếu loyalty ID
- Kỳ vọng phân quyền: key user xem log sync, admin retry
- Báo cáo / chứng từ liên quan: sync log report
- Acceptance criteria: trạng thái sync được theo dõi đầy đủ và retry hoạt động đúng

## 7. Yêu Cầu Phi Chức Năng Và Tích Hợp

- Tích hợp CRM cần có cơ chế log request/response ở mức nghiệp vụ.
- Tích hợp loyalty cần retry có kiểm soát và phân biệt timeout với lỗi dữ liệu.
- Chỉ người có quyền mới xem hoặc xử lý approval và sync failures.
- Các trạng thái chính phải hiển thị rõ trên màn hình vận hành để key user theo dõi.

## 8. Kế Hoạch Chuyển Đổi Dữ Liệu (Sơ bộ)

- Import customer master kèm CRM external ID
- Import mapping loyalty ID nếu có
- Làm sạch sales team và approver mapping trước UAT
- Cung cấp template Excel cho customer chuẩn bị dữ liệu

## 9. Phụ Lục Và Xác Nhận

### 9.1 Thuật ngữ

- SO: Sale Order
- CRM: Customer Relationship Management
- UAT: User Acceptance Test

### 9.2 Clarification baseline / applied assumptions

- `CL-001`: credit rule block khi có công nợ quá hạn hoặc vượt hạn mức
- `CL-003`: loyalty sync phase 1 dùng synchronous request/response, chưa có callback flow
- `CL-004`: nếu không có manager gán cho sales team thì regional sales director nhận approval notice

### 9.3 Sign-off

| Vai trò | Đại diện | Trạng thái xác nhận | Ghi chú |
|---|---|---|---|
| PM dự án |  | Pending |  |
| Sales key user |  | Pending |  |
| Đại diện khách hàng |  | Pending |  |
