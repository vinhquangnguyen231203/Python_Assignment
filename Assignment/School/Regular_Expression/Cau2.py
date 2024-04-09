import re

def extract_username_and_company(email):
    # Sử dụng biểu thức chính quy để trích xuất thông tin từ địa chỉ email
    match = re.match(r'^([a-zA-Z]+)@([a-zA-Z]+\.[a-zA-Z]+\.[a-zA-Z]+)$', email)
    if match:
        username = match.group(1)
        companyname = match.group(2)
        return username, companyname
    else:
        return None, None

# Hỏi người dùng nhập địa chỉ email
email = input("Nhập địa chỉ email: ")

# Trích xuất username và company name từ địa chỉ email và kiểm tra tính hợp lệ
username, companyname = extract_username_and_company(email)
if username and companyname:
    print("Username:", username)
    print("Company name (Tên miền thứ cấp và cao cấp):", companyname)
    print(f"Company name (Tên công ty): {companyname.split('.')[0]}")
    # Kiểm tra xem username và company name chỉ chứa chữ cái hay không
    if username.isalpha() and companyname.split('.')[0].isalpha():
        print("Username và Company name chỉ chứa chữ cái.")
    else:
        print("Username hoặc Company name không chỉ chứa chữ cái.")
else:
    print("Địa chỉ email không hợp lệ.")
