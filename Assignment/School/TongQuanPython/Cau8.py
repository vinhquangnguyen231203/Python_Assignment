while True:
    try:
        s = int(input('Nhập số giây: (0 để kết thúc): '))
        if (s < 0):
            print('Số giây phải lớn hơn 0')
            continue
        elif (s == 0):
            break
        h = s // 3600
        m = (s % 3600) // 60
        s = (s % 3600) % 60
        print(f'Thời gian quy đổi là {h}:{m}:{s}')
    except ValueError:
        print("Vui long nhap so nguyen")
print('Kết thúc chương trình!! ')