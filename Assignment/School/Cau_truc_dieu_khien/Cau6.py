while True:
    try:
        a = int(input('Nhập a: '))
        b = int(input('Nhập b: '))
        if(a > b):
            print(f'{a} lon hon {b}')
        elif (a < b):
            print(f'{a} nhỏ hon {b}')
        else:
            print(f'{a} bang {b}')
    except ValueError:
        print('Vui lòng nhập số')