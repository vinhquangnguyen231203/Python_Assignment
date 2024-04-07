# Nhập điểm của ba môn cùng một lúc và sử dụng eval() để chuyển đổi chuỗi nhập thành các giá trị số
diem_toan, diem_ly, diem_hoa = eval(input("Nhập điểm các môn Toán, Lý, Hoá (cách nhau bằng dấu phẩy): "))

# Xuất điểm từng môn
print("Điểm môn Toán:", diem_toan)
print("Điểm môn Lý:", diem_ly)
print("Điểm môn Hoá:", diem_hoa)

# Tính điểm trung bình ba môn
diem_trung_binh = (diem_toan + diem_ly + diem_hoa) / 3

# Xuất điểm trung bình
print("Điểm trung bình ba môn:", diem_trung_binh)
