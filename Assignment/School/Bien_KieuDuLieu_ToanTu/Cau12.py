s1 = input('Nhập vào chuỗi s1: ')
s2 = input('Nhập vào chuỗi s2: ')

if(s2 in s1):
    print(f'{s2} là chuỗi con {s1}')
elif (s1 in s2):
    print(f'{s1} là chuỗi con {s2}')
else:
    print(f'{s1} và {s2} khác nhau')