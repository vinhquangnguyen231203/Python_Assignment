while True:
    try:
        n = int(input('Nhập vào n: '))
        a = int(input('Nhập vào a: '))

        if(a < 0 or n < 0):
            print('Phải là số nguyên dương')
            continue
        
        count = 0
        for i in range(1,n):
            if(n % i == 0):
                count += 1
        
        print(f'{n} có dạng là {a} ^ {count}')
    except ValueError:
        print('Vui long nhap so')