def check_leep_year(year):
    if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
        return 29
    else:
        return 28
def check_month_by_year(month,year):
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    else:
        return check_leep_year(year)
while True:
    try:
        year = int(input('Nhập vào năm: '))
        month = int(input('Nhập tháng: '))
        print(f'Tháng {month} trong năm {year} co {check_month_by_year(month,year)} ngày')
    except ValueError:
        print('Vui long nhap so ')