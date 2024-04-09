import re

def valid_password(password):

    # Kiểm tra độ dài mật khẩu
    if len(password) < 6 or len(password) > 12:
        return False
    
    # Kiểm tra 1 chữ cái nằm trong [a-z]
    if not re.search("[a-z]", password):
        return False
    
    #Kiểm tra 1 số nằm trong [0-9]
    if not re.search("[0-9]",password):
        return False
    
    # Kiểm tra 1 chuỗi trong [A-Z]
    if not re.search("[A-Z]", password):
        return False
    
    # Kiểm tra 1 kiểu dữ liệu trong [$#@]
    if not re.search("[$#@]", password):
        return False
    
    # Kiểm tra mật khẩu ko chứa khoảng trắng
    if ' ' in password:
        return False
    
    return True

# Chương trình
while True:
    try:
        password = input('Nhập mật khẩu: ')
        if valid_password(password):
            print('Mật khẩu hợp lệ!')
        else:
            print('Mật khẩu ko hợp lệ!')

        check = input('Bạn có muốn tiếp tục (y/n): ')
        check = check.strip().lower()
        if(check == 'n' or check == 'no'):
            break
    except UnicodeEncodeError:
        print('Mật khẩu chứa ký tự unicode - nhập lại')
print('Kết thúc chương trình')
