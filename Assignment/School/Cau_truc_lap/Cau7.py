while True:
    try:
        num = [int(input('Nhập vào các số thứ {i+1}')) for i in range(5)]

        for numbers in num:
            if(numbers < 0 or numbers > 10):
                raise ValueError('Các số thứ phải nằm trong khoảng từ 0 đến 10')
            
        average_score = sum(num) / len(num)

        print(f'ĐTB là : {average_score}')
    except ValueError:
        print('Vui long nhap so')