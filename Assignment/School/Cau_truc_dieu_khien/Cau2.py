def ranking(diem):
    if(diem >= 9):
        return 'Giỏi'
    elif(diem >= 7) :
        return 'Kha'
    elif(diem >= 6):
        return 'Trung bình khá'
    elif(diem >= 5):
        return 'Trung bình'
    else:
        return 'Yếu'
while True:
    try:
        diem = float(input('Nhập diem: '))
        if (diem < 0 or diem > 10):
            print('Diem phải lớn hơn 0 va nho hơn 10')
            continue
        check_ur_rank = ranking(diem)
        print(f'Xep loai cua ban la: {check_ur_rank}')
    except ValueError:
        print('Vui lòng nhập điểm dạng số float')