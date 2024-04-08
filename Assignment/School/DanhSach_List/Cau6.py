fullName = input('Nhập vào họ và tên: ')

fullName_split = fullName.split(' ')
lenght = len(fullName_split)
if(lenght == 1):
    print(f'Tên: {fullName}')
elif(lenght == 2):
    print(f'Họ là: {fullName_split[0]}')
    print(f'Tên là: {fullName_split[1]}')
else:
    print(f'Họ là: {fullName_split[0]}')
    print(f'Lót tên là: {" ".join(fullName_split[1:-1])}')
    print(f'Tên là: {fullName_split[-1]}')