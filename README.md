# 🌳 Hệ Thống Quản Lý Sinh Viên - Mô phỏng B-Tree Indexing trong Cơ Sở Dữ Liệu

Một ứng dụng web minh họa trực quan cách các hệ quản trị cơ sở dữ liệu (như MySQL, PostgreSQL) sử dụng cấu trúc dữ liệu **B-Tree** làm Secondary Index để tăng tốc độ truy xuất dữ liệu. 

Dự án được viết hoàn toàn bằng **Vanilla HTML, CSS và JavaScript** (Không sử dụng thư viện/framework bên thứ 3). Đặc biệt tích hợp hiệu ứng **FLIP Animation** giúp người dùng quan sát mượt mà quá trình di chuyển, tách (split) và gộp (merge) các Node trên cây.

## ✨ Tính năng nổi bật

* **Minh họa B-Tree Trực quan (B-Tree Visualization):** Hiển thị sơ đồ cây thời gian thực. Bậc của cây (Degree) có thể tùy chỉnh.
* **Hiệu ứng FLIP Mượt mà:** Các con số (Mã SV) sẽ tự động trượt, nảy và sắp xếp lại vị trí mỗi khi cấu trúc cây thay đổi (Thêm/Xóa Node).
* **Thao tác CRUD Cơ bản:** Thêm, xóa sinh viên. Các thao tác này sẽ cập nhật đồng thời trên Bảng dữ liệu gốc và Chỉ mục B-Tree.
* **So sánh Thuật toán Tìm kiếm:**
    * *Tìm theo Mã SV:* Sử dụng **B-Tree Index**, trỏ thẳng đến địa chỉ vật lý với độ phức tạp $O(\log n)$.
    * *Tìm theo Họ Tên:* Không có Index, hệ thống bắt buộc thực hiện **Full Table Scan** (Quét toàn bộ bảng) với độ phức tạp $O(n)$.
* **Import Data từ CSV:** Hỗ trợ nạp hàng nghìn dữ liệu sinh viên cùng lúc thông qua file `.csv`.

## 🧠 Nguyên lý hoạt động (Under the Hood)

Ứng dụng chia làm 2 thành phần chính để mô phỏng một Database thực thụ:
1.  **Bảng Dữ liệu Gốc (Base Table):** Lưu trữ toàn bộ thông tin sinh viên (Họ tên, Giới tính). Mỗi bản ghi được cấp phát một `Pointer` (Ví dụ: `0x1005`) mô phỏng địa chỉ bộ nhớ vật lý trên ổ cứng.
2.  **Chỉ mục B-Tree (Index):** Chỉ lưu trữ Key (`Mã SV`) và Value (`Pointer`). Cấu trúc cây giúp thu hẹp phạm vi tìm kiếm cực nhanh. Khi tìm thấy Mã SV trên cây, hệ thống lấy `Pointer` đó để truy xuất chính xác 1 dòng duy nhất dưới Bảng Gốc.