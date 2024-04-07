NhanVien = ['Trần An Bình', 'Nguyễn Trần Hương Khê', 'Mai Hữu Khanh', 'Lê Minh Tâm',
            'Nguyễn Văn Tài', 'Ngô Ngọc Vân', 'Trần Thị Thanh Loan', 'Mai Anh Dũng',
            'Lê Thị Thanh Nga', 'Ngô Tuyết Loan', 'Lý Minh Hiển', 'Lâm Thành Trí',
            'Hoàng Lê Minh Trí', 'Nguyễn Hoàng Nam', 'Lê Ngọc Minh Thy', 'Hoàng Anh Quân',
            'Lâm Quốc Khanh', 'Lý Thuỵ Hoàng Uyên', 'Lâm Nguyễn Hương Giang', 'Nguyễn Hồng Vân',
            'Đỗ Quốc Bình', 'Lương Thành Tâm', 'Lương Ngọc Ái Loan', 'Đỗ Hùng Dũng']

while True:
    key = input('Nhập tên nhân viên cần tìm: (để trống hoặc rỗng để kết thúc): ')
    # Thoát chương trình nếu rỗng hoặc trống
    if not key.strip():
        break
    
    # Tạo danh sách rỗng chứa nv tìm dc
    list_timThay = []



    for nhanvien in NhanVien:
        last_Name = nhanvien.split()[-1]
        if key.lower().split()[-1] == last_Name.lower().strip():
            list_timThay.append(nhanvien)

    STT = 1;
    if list_timThay:
        print(f'Các nhân viên có tên "{key}" là:')
        for i in list_timThay:
            print(f'{STT} - ', i)
            STT+=1
    else:
        print(f'Không có nhân viên nào có tên "{key}" trong danh sách.')

print('\n Kết thúc chương trình')
