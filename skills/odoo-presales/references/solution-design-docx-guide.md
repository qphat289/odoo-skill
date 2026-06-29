# Solution Design DOCX Guide

Use this guide to create the Vietnamese `Solution Design.docx` artifact for customer, project team, FC lead, PM, solution owner, and technical lead review.

## Purpose

Explain the selected Odoo solution at a decision level: what approach is chosen, why it is chosen, what is standard/config/custom/integration/process change, and what risks, dependencies, or confirmations affect delivery.

Solution Design is not a full functional specification and not a code-level technical design.

## Language and format

- Write in Vietnamese unless the user requests another language.
- Deliver as `.docx`.
- Use the document runtime skill/capability for DOCX creation, editing, rendering, and visual QA when available.
- Keep the tone business-facing and decision-oriented.

## Canonical structure

Use this section order unless the user provides a stronger customer template:

```markdown
# Solution Design

## 1. Tóm Tắt Giải Pháp

## 2. Mục Tiêu Và Phạm Vi
### 2.1 In Scope
### 2.2 Out Of Scope
### 2.3 Nguyên tắc ra quyết định

## 3. Bức Tranh Giải Pháp Tổng Thể
### 3.1 Solution overview
### 3.2 Phân hệ tham gia
### 3.3 Luồng dữ liệu / vai trò chính

## 4. Bản Đồ Giải Pháp Theo Nhóm Yêu Cầu

| Nhóm yêu cầu | Nghiệp vụ | Standard | Configuration | Customization | Integration | Process Change | Ghi chú |
|---|---|---|---|---|---|---|---|

## 5. Tóm Tắt Quyết Định Fit/Gap

## 6. Phương Án Giải Pháp Được Chọn
### 6.x [Tên nhóm nghiệp vụ]
#### 6.x.1 Nhu cầu hiện tại
#### 6.x.2 Phương án được chọn
#### 6.x.3 Lý do chọn
#### 6.x.4 Các phương án không chọn
#### 6.x.5 Tác động lên người dùng / quy trình / dữ liệu

## 7. Tích Hợp Và Luồng Dữ Liệu Tổng Thể

## 8. Phân Quyền, Kiểm Soát Và Tuân Thủ

## 9. Chuyển Đổi Dữ Liệu Và Cutover

## 10. Phân Kỳ Triển Khai

## 11. Rủi Ro, Giả Định, Phụ Thuộc

## 12. Confirmation Baseline And Applied Assumptions

## 13. Sign-Off / Review Notes
```

## Mandatory section intent

### 1. Tóm Tắt Giải Pháp

This is the executive summary for customer and delivery stakeholders.

Include:

- mục tiêu của giải pháp
- những gì dùng chuẩn Odoo
- những gì cần cấu hình
- những gì cần customize hoặc integration
- những điểm rủi ro hoặc cần xác nhận sớm

Keep it short, readable, and decision-focused.

### 2. Mục Tiêu Và Phạm Vi

This section aligns solution boundaries with signed scope.

Include:

- in-scope solution areas
- out-of-scope or later-phase areas
- nguyên tắc lựa chọn giải pháp, ví dụ: ưu tiên standard trước custom, tối thiểu hóa thay đổi quy trình khi hợp lý, tránh tạo phụ thuộc vận hành khó kiểm soát

### 3. Bức Tranh Giải Pháp Tổng Thể

Define the overall solution shape before diving into decision details.

Typical content:

- các phân hệ Odoo tham gia
- hệ thống ngoài nếu có
- vai trò business chính
- dữ liệu hoặc trigger đi giữa các bước chính
- điểm nào là standard flow, điểm nào là extension

### 4. Bản Đồ Giải Pháp Theo Nhóm Yêu Cầu

This is the main classification map for readers who need a concise view.

Use a table like:

```markdown
| Nhóm yêu cầu | Nghiệp vụ | Standard | Configuration | Customization | Integration | Process Change | Ghi chú |
|---|---|---|---|---|---|---|---|
| Approval | Phê duyệt đơn bán hàng | một phần | threshold config | approval flow | không | không | cần trạng thái chờ duyệt |
```

Rules:

- one row should represent one requirement group or decision group
- do not dump every fit-gap row if the document becomes noisy
- keep wording understandable to business stakeholders

### 5. Tóm Tắt Quyết Định Fit/Gap

This section is the business-facing decision summary, not the raw XLSX workbook.

Use it to explain:

- nhóm nào fit hoàn toàn
- nhóm nào cần cấu hình
- nhóm nào cần custom
- nhóm nào cần tích hợp
- nhóm nào yêu cầu thay đổi quy trình vận hành

### 6. Phương Án Giải Pháp Được Chọn

This is the core decision section.

For each major area, include:

- nhu cầu hiện tại
- phương án được chọn
- vì sao chọn phương án đó
- phương án nào đã xem nhưng không chọn
- tác động đến người dùng, quy trình, dữ liệu, trách nhiệm vận hành

Recommended decision block:

```markdown
### 6.1 Phê duyệt đơn bán hàng

#### 6.1.1 Nhu cầu hiện tại
#### 6.1.2 Phương án được chọn
#### 6.1.3 Lý do chọn
#### 6.1.4 Các phương án không chọn
#### 6.1.5 Tác động lên người dùng / quy trình / dữ liệu
```

### 7. Tích Hợp Và Luồng Dữ Liệu Tổng Thể

Capture:

- hệ thống nào kết nối với Odoo
- chiều dữ liệu đi / về
- trigger nghiệp vụ
- tần suất đồng bộ
- trách nhiệm xử lý lỗi ở góc nhìn vận hành

### 8. Phân Quyền, Kiểm Soát Và Tuân Thủ

Keep this at policy level, not ACL/XML detail.

Include:

- nhóm vai trò chính
- điểm kiểm soát / phê duyệt
- yêu cầu audit trail hoặc log
- ràng buộc bảo mật / tuân thủ nếu có

### 9. Chuyển Đổi Dữ Liệu Và Cutover

Summarize what the solution needs for go-live readiness:

- dữ liệu cần chuẩn bị
- điều kiện cutover
- dữ liệu mapping bắt buộc
- hoạt động đối soát sau go-live nếu có

### 10. Phân Kỳ Triển Khai

Use this section when the scope spans phases or waves.

Include:

- phase 1 / phase 2 boundaries
- dependencies between phases
- criteria to move later items out of current scope

### 11. Rủi Ro, Giả Định, Phụ Thuộc

Make hidden risk visible.

Typical content:

- giả định từ phía khách hàng
- phụ thuộc hệ thống ngoài
- phụ thuộc quyết định key user
- rủi ro nếu không xác nhận đúng hạn

### 12. Confirmation Baseline And Applied Assumptions

Use this section to summarize the clarified business inputs that the chosen solution depends on.

Recommended table:

```markdown
| ID | Clarification Ref | Confirmed input / applied assumption | Impact on solution | Status |
|---|---|---|---|---|
| SD-CF-01 | CL-001 | Credit blocking uses overdue amount or exceeded limit | drives approval and validation design | Confirmed |
```

### 13. Sign-Off / Review Notes

Use for:

- reviewer comments summary
- sign-off state
- danh sách bên cần xác nhận

## Solution decision rules

1. Choose a solution only for requirements already in scope or explicitly under review.
2. Do not add optional features unless the user asks for recommendations.
3. Explain why standard/config/custom/integration/process-change treatment is appropriate.
4. Keep rejected alternatives concise and decision-oriented.
5. Resolve or explicitly waive business-facing open decisions in `Clarification Register.xlsx` before finalizing the document; this document should summarize confirmed inputs, not act as the question backlog.
6. Separate customer-approved scope from internal future ideas.
7. Keep the document understandable to FC, PM, customer, and technical lead at the same time.

## Inputs

- Scope of Work or customer requirements
- `Requirement Analysis.md`
- `Fit-Gap Analysis.xlsx`
- `Functional Design.docx` draft or approved version
- Technical constraints from dev/technical consultant when available

## Recommended companion files

- `skills/odoo-presales/references/functional-design-docx-guide.md`
- `skills/odoo-presales/references/solution-design-example-sale-approval.md`
- `Technical Design.md`

## Output quality gates

- every major solution decision maps to a requirement or fit-gap group
- standard/config/custom/integration/process-change boundaries are clear
- customer responsibilities and dependencies are visible
- clarified inputs that materially affect the solution are explicit
- the document does not collapse into raw fit-gap rows or technical implementation notes
