s1 = input('Nhập vào chuỗi 1: ')
s2 = input('Nhập vào chuỗi 2: ')
s3 = input('Nhập vào chuỗi 3: ')

print("# Cách 1: f-string")
print(f'{s1:^35} {s2:^35} {s3:^35}')

print("# Cách 2: %-format")
print('%-35s %-35s %-35s' % (s1, s2, s3))

print("# Cách 3: .format")
print('{:^35} {:^35} {:^35}'.format(s1, s2, s3))