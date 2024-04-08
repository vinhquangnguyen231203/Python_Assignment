name = input('Nhập họ và tên: ')
name_split = name.split(' ');
name_reverse = name_split[::-1]

print(f'Chuỗi đảo ngược: {" ".join(name_reverse)}')
