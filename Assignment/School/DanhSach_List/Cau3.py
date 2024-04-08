while True:
    try:
        Dong = int(input('Nhập vào số dòng: '))
        Cot = int(input('Nhập vào số cột: '))
        matrix = []
        for i in range (Dong):
            row = []
            for j in range (Cot):
                row.append(i*j)
            matrix.append(row)

        print("Mảng 2 chiều:")
        for row in matrix:
            print(row)
    except ValueError:
        print('Vui long nhap so')