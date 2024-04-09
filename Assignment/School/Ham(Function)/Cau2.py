chuoi = input('Nhập chuỗi: ')

def reverse_string(chuoi):
    chuoi_split = chuoi.split(' ')
    chuoi_reverse =" ".join(chuoi_split[::-1])
    return chuoi_reverse

print(f'Chuỗi đảo ngược: {reverse_string(chuoi)}')