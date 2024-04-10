
def menu():
    print("+" + "-"*60 + "+")
    print("|\033[1;32m"  +" "*5+ "Chương trình quản lý đăng ký số điện thoại:" + " "*12 + "\033[0m|")
    print("|" + "-"*60 + "|")
    print("|" + " "*60 + "|")
    print("|\033[1;34m 1: Đăng ký số điện thoại" + " "*35 + "\033[0m|")
    print("|\033[1;34m 2: Sửa chi tiết" + " "*44 + "\033[0m|")
    print("|\033[1;34m 3: Xoá số điện thoại" + " "*39 + "\033[0m|")
    print("|\033[1;34m 4: Xem danh sách theo đầu số" + " "*31 + "\033[0m|")
    print("|\033[1;34m 5: Xem dữ liệu thô trong file" + " "*30 + "\033[0m|")
    print("|\033[1;91m 0: Thoát khỏi chương trình" + " "*33 + "\033[0m|")
    print("+" + "-"*60 + "+")
    print("\n")

def read_data():
    data = []
    try:
        with open("DuLieu.txt", "r", encoding="UTF-8") as file:
            for line in file:
                data.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    return data

def write_data(data):
    with open("Dulieu.txt", "w") as file:
        for record in data:
            file.write(",".join(record) + "\n")

def Iscontinue(fc):
    while True:
        try:
            print("\n")
            lua_chon = int(input("\033[93mBạn có muốn tiếp tục không? Nhấn 1 để tiếp tục, 0 để thoát, 2 để trả về giao diện ban đầu:\033[0m"))
            print("\n")
            if lua_chon == 1:
                return fc()
            elif lua_chon == 2:
                return menu()
            elif lua_chon ==0:
                return exit()
            else:
                print("\033[91mVui lòng nhập số 1 hoặc 0.\033[0m")
                print("\n")
        except ValueError:
            print("\n")
            print("\033[91mVui lòng chỉ nhập số nguyên.\033[0m")
            print("\n")


def add_record():
    data = read_data()
    
    while True:
        phone_number = input("Nhập số điện thoại cần đăng kí: ")
        if phone_number.isdigit() and len(phone_number) == 10 and phone_number.startswith('0'):
            break
        else:
            print("\033[1;31mNhập sai định dạng.Số điện thoại phải chứa đúng 10 kí tự số và bắt đầu từ số 0\033[0m")

    for record in data:
        if record[0] == phone_number:
            print("\033[1;31mSố điện thoại đã tồn tại, vui lòng đăng kí số khác\033[0m")
            return add_record()

    name = input("Nhập họ và tên: ")
    while not name or not name.strip() or not name.replace(" ", "").isalpha():  
        print("\033[1;31mTên không được để trống và phải chứa chỉ các kí tự chữ cái.\033[0m")
        name = input("Nhập họ và tên: ")
    
    address = input("Nhập địa chỉ: ")
    while not address:
        print("\033[1;31mĐịa chỉ không được để trống.\033[0m")
        address = input("Nhập địa chỉ: ")

    while True:
        gender = input("Nhập giới tính (Nam/Nu): ").lower()
        if gender in ['nam', 'nu']:
            break
        else:
            print("\033[1;31mGiới tính chỉ được nhập Nam hoặc Nữ, không phân biệt chữ hoa thường.\033[0m")

    while True:
        cccd = input("Nhập số CCCD (chỉ 12 kí tự số): ")
        if cccd.isdigit() and len(cccd) == 12:
            break
        else:
            print("\033[1;31mCCCD phải chứa đúng 12 kí tự số.\033[0m")
    new_record = [phone_number, name, address, gender, cccd]
    data.append(new_record)
    
    write_data(data)
    print("\033[1;37mĐã thêm đăng ký số điện thoại.\033[0m")
    print("\n")
    print(f"\n\033[1mThông tin vừa đăng kí:\033[0m")
    print("\033[1m+" + "-" * 62 + "+""\033[0m")
    print(f"|\033[1;34m Số điện thoại: {new_record[0]:<45} \033[0m|")
    print(f"|\033[1;34m Họ và tên: {new_record[1]:<49} \033[0m|")
    print(f"|\033[1;34m Địa chỉ: {new_record[2]:<51} \033[0m|")
    print(f"|\033[1;34m Giới tính: {new_record[3]:<49} \033[0m|")
    print(f"|\033[1;34m Số CCCD: {new_record[4]:<51} \033[0m|")
    print("\033[1m+" + "-" * 62 +"+" "\033[0m")



    print("\n")

    Iscontinue(add_record)

def edit_record():
    data = read_data()
    phone_number = input("Nhập số điện thoại cần sửa: ")
    for record in data:
        if record[0] == phone_number:
            
            print(f"\033[1mThông tin của số điện thoại {phone_number}:\033[0m")
            print("\033[1m" +"+"+ "-" * 62 + "+""\033[0m")
            print(f"|\033[1;34m Số điện thoại: {record[0]:<45} \033[0m|")
            print(f"|\033[1;34m Họ và tên: {record[1]:<49} \033[0m|")
            print(f"|\033[1;34m Địa chỉ: {record[2]:<51} \033[0m|")
            print(f"|\033[1;34m Giới tính: {record[3]:<49} \033[0m|")
            print(f"|\033[1;34m Số CCCD: {record[4]:<51} \033[0m|")
            print("\033[1m" +"+"+ "-" * 62 +"+" "\033[0m")
            record[1] = input("Nhập họ và tên mới: ")
            while not record[1].replace(" ", "").isalpha():
                print("\033[1;31mHọ và tên phải chứa chỉ các kí tự chữ cái.\033[0m")
                record[1] = input("Nhập họ và tên mới: ")

            record[2] = input("Nhập địa chỉ mới: ")
            while not record[2]:
                print("\033[1;31mĐịa chỉ không được để trống.\033[0m")
                record[2] = input("Nhập địa chỉ mới: ")

            while True:
                gender = input("Nhập giới tính mới (Nam/Nu): ").lower()
                if gender in ['nam', 'nu']:
                    record[3] = gender
                    break
                else:
                    print("\033[1;31mGiới tính chỉ có thể là 'Nam' hoặc 'Nu'.\033[0m")

            record[4] = input("Nhập số CCCD mới: ")
            while not record[4].isdigit() or len(record[4]) != 12:
                print("\033[1;31mSố CCCD phải là một chuỗi gồm 12 kí tự số.\033[0m")
                record[4] = input("Nhập số CCCD mới: ")

            write_data(data)
            print("Đã cập nhật thông tin.")
            print(f"\033[1mThông tin của số điện thoại {phone_number} sau khi cập nhật là: \033[0m")
            print("\033[1m" +"+"+ "-" * 62 + "+""\033[0m")
            print(f"|\033[1;34m Số điện thoại: {record[0]:<45} \033[0m|")
            print(f"|\033[1;34m Họ và tên: {record[1]:<49} \033[0m|")
            print(f"|\033[1;34m Địa chỉ: {record[2]:<51} \033[0m|")
            print(f"|\033[1;34m Giới tính: {record[3]:<49} \033[0m|")
            print(f"|\033[1;34m Số CCCD: {record[4]:<51} \033[0m|")
            print("\033[1m" +"+"+ "-" * 62 +"+" "\033[0m")
            print("\n")
            Iscontinue(edit_record)
            return
        
    print("\033[1;31mKhông tìm thấy số điện thoại.\033[0m")
    print("\n")
    Iscontinue(edit_record)



def delete_record():
    data = read_data()
    phone_number = input("Nhập số điện thoại cần xoá: ")
    for record in data:
        if record[0] == phone_number:
            choice = input("Bạn muốn xóa thông tin này vĩnh viễn (nhấn 1) hay tạm thời (nhấn 2)? ")
            if choice == '1':
                data.remove(record)
                write_data(data)
                print("Đã xoá đăng ký số điện thoại vĩnh viễn.")
                print("\n")
                print("\033[1mThông tin đã bị xóa:\033[0m")
                print("\033[1m" +"+"+ "-" * 62 + "+""\033[0m")
                print(f"|\033[1;34m Số điện thoại: {record[0]:<45} \033[0m|")
                print(f"|\033[1;34m Họ và tên: {record[1]:<49} \033[0m|")
                print(f"|\033[1;34m Địa chỉ: {record[2]:<51} \033[0m|")
                print(f"|\033[1;34m Giới tính: {record[3]:<49} \033[0m|")
                print(f"|\033[1;34m Số CCCD: {record[4]:<51} \033[0m|")
                print("\033[1m" +"+"+ "-" * 62 +"+" "\033[0m")
                print("\n")
                Iscontinue(delete_record)
                return
            elif choice == '2':
                deleted_record = None  # Biến để lưu trữ thông tin của bản ghi bị xoá

                new_data = []
                for record in data:
                    if record[0] == phone_number:
                        deleted_record = record  # Lưu thông tin của bản ghi bị xoá
                        print("\n")
                        print("\033[1mThông tin đã bị xóa:\033[0m")
                        print("\033[1m" +"+"+ "-" * 62 + "+""\033[0m")
                        print(f"|\033[1;34m Số điện thoại: {record[0]:<45} \033[0m|")
                        print(f"|\033[1;34m Họ và tên: {record[1]:<49} \033[0m|")
                        print(f"|\033[1;34m Địa chỉ: {record[2]:<51} \033[0m|")
                        print(f"|\033[1;34m Giới tính: {record[3]:<49} \033[0m|")
                        print(f"|\033[1;34m Số CCCD: {record[4]:<51} \033[0m|")
                        print("\033[1m" +"+"+ "-" * 62 +"+" "\033[0m")
                        print("\n")
                    else:
                        new_data.append(record)

                if deleted_record:
                     # Ghi thông tin của bản ghi đã xoá vào tệp Delete_DuLieu.txt
                    with open("Delete_DuLieu.txt", "a") as delete_file:
                        delete_file.write(",".join(deleted_record) + "\n")

                    # Ghi lại dữ liệu còn lại vào tệp DuLieu.txt
                    write_data(new_data)

                    print("\033[1mĐã xoá đăng kí số điện thoại tạm thời (thông tin bản ghi vẫn được lưu trong file Delete_DuLieu.txt).\033[0m")
                   
                Iscontinue(delete_record)
                return
            else:
                print("\033[1;31mLựa chọn không hợp lệ.\033[0m")
                delete_record()  # Gọi lại hàm nếu lựa chọn không hợp lệ
                return
    print("\033[1;31mKhông tìm thấy số điện thoại.\033[0m")
    print("\n")
    Iscontinue(delete_record)



def view_by_prefix():
    data = read_data()

    print("Danh sách các đầu số điện thoại đã đăng kí:")
    printed_numbers = set()  # ????????Tạo một set để lưu các số điện thoại đã được in ra

    for record in data:
        phone_number_prefix = record[0][:4]  # Lấy 4 số đầu của số điện thoại
        if phone_number_prefix not in printed_numbers:
            print(phone_number_prefix)  # In ra chỉ 4 số đầu của số điện thoại
            printed_numbers.add(phone_number_prefix)  # Thêm số điện thoại vào set đã in ra

    prefix = input("Nhập đầu số cần xem: ")
    
    matching_records = [record for record in data if record[0].startswith(prefix)]
    if matching_records:
        print("Danh sách số điện thoại thuộc đầu số", prefix + " là:")
        print("\n")
        for record in matching_records:
            print("\033[1m" +"+"+ "-" * 62 + "+""\033[0m")
            print(f"|\033[1;34m Số điện thoại: {record[0]} - Họ tên: {record[1]:<24} \033[0m|")
            print(f"|\033[1;34m Địa chỉ: {record[2]:<51} \033[0m|")
            print(f"|\033[1;34m Giới tính: {record[3]:<14} - CCCD: {record[4]:<26} \033[0m|")
            print("\033[1m" +"+"+ "-" * 62 +"+" "\033[0m")
        print("\n")
        print("Tổng số lượng số điện thoại thuộc đầu số", prefix + ":", len(matching_records))
    else:
        print("\033[1;31mKhông có số điện thoại nào thuộc đầu số\033[0m", prefix)
    
    print("\n")

    Iscontinue(view_by_prefix)


def view_raw_data():
    data = read_data()
    print("\033[1mDữ liệu thô trong file:\033[0m")
    print("-"*160)
    for record in data:
        phone_number = record[0]
        name = record[1]
        address = record[2]
        gender = record[3]
        cccd = record[4]

        # Tính toán số lượng ký tự khoảng trắng cần thêm vào để căn chỉnh
        padding_phone = " " * (12 - len(phone_number))
        padding_name = " " * (30 - len(name))
        padding_address = " " * (30 - len(address))
        padding_gender = " " * (5- len(gender))
        padding_cccd = " " * (15 - len(cccd))

        # Hiển thị dữ liệu với các ký tự khoảng trắng căn chỉnh
        formatted_record = f"\033[1;32mSố điện thoại:\033[0m {phone_number}{padding_phone} | " \
                           f"\033[1;34mHọ tên:\033[0m {name}{padding_name} | " \
                           f"\033[1;36mĐịa chỉ:\033[0m {address}{padding_address} | " \
                           f"\033[1;33mGiới tính:\033[0m {gender}{padding_gender} | " \
                           f"\033[1;35mSố CCCD:\033[0m {cccd}{padding_cccd}"

        print(formatted_record)
    print("-"*160)
    print("\n")

    Iscontinue(view_raw_data)

