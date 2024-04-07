while True:
    try:
        a = int(input('Nhay vao so nguyen: '))
        b = int(input('Nhay vao so nguyen: '))
        if( a <=0 or b <=0):
            print('Vui long nhap so nguyen duong')
            continue
        phanNguyen = a // b
        phanDu = a % b
        print(f'Phần nguyên là: {phanNguyen} | Phần dư là: {phanDu}')
    except ValueError:
        print('Vui lòng nhập số')
