while True:
    try:
        luong = float(input('Nhập lương: '))
        if(luong < 0):
            print('Luong phai lon hon 0')
            continue
        chucVu = input('Nhập chức vụ: ')
        chucVu = chucVu.lower()
        heSoLuong = 1.0
        if(chucVu == 'gđ'):
            heSoLuong = 2.5
        elif (chucVu == 'pgđ' or chucVu == 'tp'):
            heSoLuong = 2.0
        else:
            heSoLuong = 1.0
        print(f'Lương lĩnh: {heSoLuong * luong}')
    except ValueError:
        print('Vui lòng nhập lương là số')