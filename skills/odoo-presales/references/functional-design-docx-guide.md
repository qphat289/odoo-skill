# Functional Design DOCX Guide

Use this guide to create the Vietnamese `Functional Design.docx` artifact for customer, FC, PM, QA, key users, and delivery-team review.

This guide now absorbs the structure of the original FSD sample template, so a separate `.docx` template file is optional rather than required.

## Purpose

Describe what the business process and user-facing system behavior must be. Keep it business-readable, reviewable, and testable. Do not turn it into a code implementation plan or a delivery backlog.

## Language and format

- Write in Vietnamese unless the user requests another language.
- Deliver as `.docx`.
- Use the document runtime skill/capability for DOCX creation, editing, rendering, and visual QA when available.
- Preserve professional document structure: document control, version history, clear heading hierarchy, deliberate tables, and sign-off space.

## Canonical structure

Use this section order unless the user provides a stronger customer template:

```markdown
# Functional Design

## 1. Thông Tin Tổng Quan (Document Control)
### 1.1 Thông tin dự án
### 1.2 Lịch sử thay đổi
### 1.3 Tài liệu tham chiếu

## 2. Phạm Vi Phân Tích Và Đối Tượng Sử Dụng (Scope & Audience)
### 2.1 In Scope
### 2.2 Out Of Scope
### 2.3 Đối tượng sử dụng tài liệu

## 3. Kiến Trúc Tổng Thể Và Dữ Liệu Master (Architecture & Master Data)
### 3.1 Cấu trúc tổ chức
### 3.2 Master data
### 3.3 Quy ước dữ liệu chính

## 4. Phân Tích Quy Trình Nghiệp Vụ Chi Tiết (To-Be Business Processes)
### 4.x Quy trình [Tên quy trình]
#### 4.x.1 Mục tiêu quy trình
#### 4.x.2 Sơ đồ quy trình To-Be
#### 4.x.3 Bảng bước thực hiện
#### 4.x.4 Business rules
#### 4.x.5 Exception handling

## 5. Phân Tích Khoảng Cách Và Giải Pháp (Fit/Gap Summary)

## 6. Yêu Cầu Chức Năng Chi Tiết (Functional Requirements)
### FR-xxx [Tên yêu cầu]

## 7. Yêu Cầu Phi Chức Năng Và Tích Hợp

## 8. Kế Hoạch Chuyển Đổi Dữ Liệu (Sơ bộ)

## 9. Phụ Lục Và Xác Nhận
### 9.1 Thuật ngữ
### 9.2 Clarification baseline / applied assumptions
### 9.3 Sign-off
```

## Mandatory section intent

### 1. Thông Tin Tổng Quan

This is the document-control block. It should let customer and internal team understand:

- tên dự án
- tên khách hàng
- tên tài liệu
- phạm vi tài liệu
- trạng thái tài liệu: Draft / Review / Approved
- người soạn, người review, người phê duyệt

Use a version-history table like:

```markdown
| Phiên bản | Ngày | Người thực hiện | Nội dung thay đổi | Trạng thái |
|---|---|---|---|---|
| v0.1 | 2026-06-25 | FC / BA | Khởi tạo tài liệu | Draft |
```

### 2. Phạm Vi Phân Tích Và Đối Tượng Sử Dụng

This section exists to stop scope drift.

Include:

- quy trình hoặc nhóm chức năng nằm trong phạm vi
- hạng mục ngoài phạm vi hoặc để phase sau
- đối tượng đọc tài liệu: FC, PM, Dev, QA/QC, key users, khách hàng

### 3. Kiến Trúc Tổng Thể Và Dữ Liệu Master

Define the operating frame before detailed process content.

Typical content:

- cấu trúc công ty / chi nhánh / kho / phòng ban
- dữ liệu master liên quan
- quy tắc mã hóa hoặc quy ước dữ liệu
- đối tác, sản phẩm, UoM, location, warehouse, approval roles

### 4. Phân Tích Quy Trình Nghiệp Vụ Chi Tiết

This is the core of the FSD.

For each major process, include:

- mục tiêu quy trình
- actor / phòng ban tham gia
- trigger / điều kiện bắt đầu
- sơ đồ swimlane nếu cần
- bảng bước xử lý
- kết quả đầu ra / chứng từ sinh ra
- business rules
- exception handling

Use a step table like:

```markdown
| Bước | Phòng ban / Vai trò | Hành động trên hệ thống | Kết quả / chứng từ sinh ra |
|---|---|---|---|
| 1 | Sales | Tạo đơn bán hàng | SO ở trạng thái Draft |
| 2 | Manager | Phê duyệt yêu cầu giảm giá | Yêu cầu được Approved / Rejected |
```

### 5. Phân Tích Khoảng Cách Và Giải Pháp

This section is the FSD-facing summary of fit-gap, not the full workbook dump.

Use a compact summary table like:

```markdown
| ID | Yêu cầu khách hàng | Khả năng đáp ứng Standard | Giải pháp đề xuất | Mức độ ưu tiên |
|---|---|---|---|---|
| GAP01 | Quy trình phê duyệt nhiều cấp | Không đủ | Customize approval flow | High |
```

Only include the fit-gap rows that materially affect process understanding, user behavior, or sign-off.

### 6. Yêu Cầu Chức Năng Chi Tiết

Each detailed functional requirement should be independently traceable.

Recommended requirement block:

```markdown
### FR-001 Phê duyệt đơn bán hàng vượt ngưỡng

- Nguồn yêu cầu: Req ID / Fit-Gap ID
- Mục tiêu nghiệp vụ:
- Actor / vai trò:
- Điều kiện đầu vào:
- Luồng chính:
- Luồng ngoại lệ:
- Trường dữ liệu liên quan:
- Validation rules:
- Kỳ vọng phân quyền:
- Báo cáo / chứng từ liên quan:
- Acceptance criteria:
```

Do not replace this with implementation notes such as model names, methods, or task breakdown.

### 7. Yêu Cầu Phi Chức Năng Và Tích Hợp

Capture:

- yêu cầu tích hợp và tần suất đồng bộ
- giao tiếp với hệ thống ngoài
- hiệu năng, bảo mật, backup, logging nếu có
- yêu cầu thông báo, email, webhook, API response expectations ở góc nhìn nghiệp vụ

### 8. Kế Hoạch Chuyển Đổi Dữ Liệu

Keep this preliminary unless the user explicitly wants a detailed migration plan.

Include:

- dữ liệu cần import
- nguồn dữ liệu
- owner chuẩn bị dữ liệu
- định dạng template
- nguyên tắc làm sạch dữ liệu

### 9. Phụ Lục Và Xác Nhận

Use this section for:

- glossary / thuật ngữ
- mockup hoặc biểu mẫu tham chiếu
- clarification baseline da chot hoac gia dinh da duoc waive tu `Clarification Register.xlsx`
- khu vực ký xác nhận

## Requirement writing rules

1. Use customer language first, then clarify with Odoo terminology where useful.
2. Keep technical implementation out unless needed to explain user-facing behavior.
3. Link each functional requirement to requirement IDs and fit-gap IDs.
4. Resolve or explicitly waive business-facing clarification items in `Clarification Register.xlsx` before drafting the finished FSD; do not hide assumptions in prose.
5. Keep UX mockups, report layouts, and process diagrams close to the requirement they explain.
6. Separate signed scope, proposed phase-2 ideas, and unresolved decisions.
7. Make every process and requirement testable by QA/QC without needing code-level detail.

## Swimlane guidance

When the FSD needs a process flow, use `process-swimlane-guide.md`. The swimlane should show departments, roles, customer, vendor, system, or external systems, not Python methods or internal code components.

## Recommended companion files

- `Requirement Analysis.md`
- `Fit-Gap Analysis.xlsx`
- `Solution Design.docx`
- `Technical Design.md`
- `skills/odoo-presales/references/functional-design-example-sale-approval.md`

## DOCX quality gates

- Render and visually inspect the document when the runtime supports DOCX rendering.
- Heading hierarchy matches the canonical section order unless the customer template overrides it.
- Tables are readable, not overcrowded, and used only where row/column comparison helps.
- Vietnamese text renders correctly.
- Each requirement has clear acceptance criteria or an explicit reason it still needs confirmation.
- Business-facing clarification dependencies are resolved or explicitly referenced back to `Clarification Register.xlsx`.
- Sign-off section is present when the artifact is intended for customer review.
