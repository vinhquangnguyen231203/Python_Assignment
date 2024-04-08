try:
    n = int(input('Nhập số n: '))
    
    #Cách 1 dùng while
    i = 0
    sum = 0;
    while(i<=n):
        sum += i;
        i+=1
    print(f'Tong dùng while:{sum}')

    # Cách 2 dùng for
    sum = 0
    for i in range (0, n+1):
        sum += i
    print(f'Tong dùng for:{sum}')
except ValueError:
    print('Vui lòng nhập số')