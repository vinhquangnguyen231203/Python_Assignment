duong_dan = input('Nhập vào đường dẫn: ')

# Thay thế dấu \ thành /
duong_dan = duong_dan.replace('\\', '/')

full_file = duong_dan.split('/')[-1]
file_extension = full_file.split('.')[-1]
file_name = full_file.split('.')[0]

print(f'File đầy đủ là: {full_file}')
print(f'Đuôi file mở rộng: {file_extension}')
print(f'Tên file: {file_name}')