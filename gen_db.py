import csv
import random

def generate_students_csv(n, filename="danhsach_sinhvien.csv"):
    # Danh sách các thành phần tên phổ biến ở Việt Nam
    ho_list = ["Nguyễn", "Trần", "Lê", "Phạm", "Hoàng", "Vũ", "Võ", "Đặng", "Bùi", "Đỗ", "Hồ", "Ngô", "Dương", "Lý"]
    
    dem_nam = ["Văn", "Hữu", "Đức", "Công", "Minh", "Quang", "Gia", "Thế", "Khắc", "Thái"]
    ten_nam = ["Dũng", "Cường", "Hải", "Phong", "Thành", "Đạt", "Tuấn", "Tú", "Hùng", "Bảo", "Nam", "Khoa", "Phát", "Long"]
    
    dem_nu = ["Thị", "Ngọc", "Thu", "Phương", "Thanh", "Bích", "Diễm", "Kim", "Nhã", "Hoài"]
    ten_nu = ["Hoa", "Lan", "Mai", "Trang", "Linh", "Thảo", "Hương", "Vy", "Anh", "Nhung", "My", "Tiên", "Yến"]

    student_ids = random.sample(range(100000, 999999), n)

    with open(filename, mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file)
        
        # Ghi dòng tiêu đề (Header)
        writer.writerow(["Mã SV", "Họ Tên", "Giới tính"])

        # Tạo và ghi từng sinh viên
        for sv_id in student_ids:
            gender = random.choice(["Nam", "Nữ"])
            ho = random.choice(ho_list)
            
            # Chọn tên đệm và tên chính phù hợp với giới tính
            if gender == "Nam":
                dem = random.choice(dem_nam)
                ten = random.choice(ten_nam)
            else:
                dem = random.choice(dem_nu)
                ten = random.choice(ten_nu)
                
            full_name = f"{ho} {dem} {ten}"
            
            # Ghi dòng dữ liệu vào CSV
            writer.writerow([sv_id, full_name, gender])

    print(f"Đã tạo thành công {n} sinh viên!")
    print(f"Tệp dữ liệu đã được lưu tại: {filename}")

# Gọi hàm và truyền vào số lượng sinh viên bạn muốn tạo (Ví dụ: 100)
so_luong_sinh_vien = 2
generate_students_csv(so_luong_sinh_vien)