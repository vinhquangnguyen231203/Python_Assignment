def chao (fullName, age):
    if(age < 18):
        print(f'Chào em: {fullName}')
    elif (age >= 18 and age < 45):
        print(f'Chào anh/chị: {fullName}')
    else:
        print(f'Chào ông/ bà: {fullName}')

fullName = input('Nhập họ và tên: ')
age = int(input('Nhập tuổi: '))
chao(fullName, age)