chuoi = input('Nhập một chuỗi: ');

def reverse_string(chuoi):
    chuoi_split = chuoi.split(' ')
    chuoi_reverse =" ".join(chuoi_split[::-1])
    return chuoi_reverse

def check_Palindrome(chuoi):
    if(chuoi == reverse_string(chuoi)):
        print(f'{chuoi} la chuỗi đảo ngược')
    else:
        print(f'{chuoi} khác chuỗi đảo ngược')

check_Palindrome(chuoi)