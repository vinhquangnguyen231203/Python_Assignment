while True:
    try:
        n = int(input('Nhập số: '))
        soLe = 0;
        soChan = 0;
        for i in range (0,n):
            if (i % 2 == 0):
                soChan += i
            else:
                soLe += i
        if(n % 2 == 0):
            print(f'Kết quả số chẵn: {soChan}')
        else:
            print(f'Kết quả số lẻ: {soLe}')
        check = input('Bạn có muốn tiếp tục (y/n): ')
        check = check.lower();
        if(check == 'no' or check == 'n'):
            break
    except ValueError:
        print('Vui lòng nhập số')
print('Kết thúc chương trình')