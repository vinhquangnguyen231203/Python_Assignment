while True:
    try:
        dtb = float(input('Diem trung bình: '))
        if(dtb >= 5):
            print('Bạn đã hoàn thành khóa học')
        else:
            print('Bạn phải thi lại')
    except ValueError:
        print('Vui long nhap so thuc')