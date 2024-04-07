try:
    x = int(input('Nhập giá trị x: '))
    binhPhuong = x**2
    lapPhuong = x**3
    print('Bình phương =', binhPhuong, 'Lap phương =', lapPhuong)
except ValueError:
    print("Vui long nhap so nguyen")