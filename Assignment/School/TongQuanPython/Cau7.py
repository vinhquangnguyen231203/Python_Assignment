import math;

while True:
    try:
        r = float(input('Nhập bán kính: '))
        if (r<=0.0):
            print('Bán kính phải lớn hơn 0', '| Vui lòng nhập lại')
            continue

        C = 2* math.pi * r
        S = math.pi * r * r

        print(f'Dien tich hình tròn là: {C:.2f} | Chu vi hình tròn là: {S:.2f}')

    except ValueError:
        print('Vui lòng nhập số thực ')