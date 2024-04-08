while True:
    try:
        soNguyen = int(input('Nhập số nguyên: '))
        j = 0;
        for i in range (1,soNguyen + 1):
            if(i % 2 != 0):
                j = j + 1
                print(f'Số lẻ thứ {j} là: {i}')
    except ValueError:
        print('Vui long nhap so ')