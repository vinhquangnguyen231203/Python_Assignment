while True:
    try:
        number = int(input('Nhập số: '))
        if(number % 2 == 0):
            print(f'{number} la số chan')
        else:
            print(f'{number} la số le')
    except ValueError:
        print('Vui lòng nhập số')