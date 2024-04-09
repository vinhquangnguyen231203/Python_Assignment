def input_student_info():
    student_info = {}

    # Nhập thông tin từ người dùng
    student_info["Mã số"] = input('Nhập mã số sinh viên: ')
    student_info["Tên"] = input('Nhập tên sinh viên: ')
    student_info["Phái"] = input('Nhập phái sinh viên: ')
    student_info["Nam sinh"] = input("Nhập năm sinh của sinh viên: ")

    return student_info

# Hàm main
def main():
    num_students = int(input('Nhập số sinh viên: '))
    students = []

    # Nhập thông tin của từng sinh viên và thêm vào danh sách
    for i in range (num_students):
        print(f'Nhập thông tin sinh viên thứ {i+1}: ')
        student_info = input_student_info()
        students.append(student_info)

    # In thông tin của tất cả sinh viên
    print('\n Thông tin của tất cả sinh viên')
    for i,students in enumerate(students,start= 1):
        print(f'Sinh viên thứ {i}: ')
        for key, value in students.items():
            print(f'{key}: {value}')
        print();

# Gọi hàm main để chạy chương trình
if __name__ == '__main__':
    main()