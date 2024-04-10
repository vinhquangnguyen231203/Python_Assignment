def menu():
    print("+" + "-"*66 + "+")
    print("|" + " "*66 + "|")
    print("|\033[1;32m"  + "Chương trình quản lý đăng ký số điện thoại:" + " "*23 + "\033[0m|")
    print("|" + "-"*66 + "|")
    print("|" + " "*66 + "|")
    print("|\033[1;34m 1: Đăng ký số điện thoại" + " "*41 + "\033[0m|")
    print("|\033[1;34m 2: Sửa chi tiết" + " "*50 + "\033[0m|")
    print("|\033[1;34m 3: Xoá số điện thoại" + " "*45 + "\033[0m|")
    print("|\033[1;34m 4: Xem danh sách theo đầu số" + " "*37 + "\033[0m|")
    print("|\033[1;34m 5: Xem dữ liệu thô trong file" + " "*36 + "\033[0m|")
    print("|\033[1;33m 0: Thoát khỏi chương trình" + " "*39 + "\033[0m|")
    print("+" + "-"*66 + "+")



def read_data():
    data = []
    try:
        with open("DuLieu.txt", "r", encoding="utf-8") as file:
            for line in file:
                data.append(line.strip().split(","))
    except FileNotFoundError:
        pass
    return data

def write_data(data):
    with open("DuLieu.txt", "w") as file:
        for record in data:
            file.write(",".join(record) + "\n")

def add_record():
    data = read_data()
    
    while True:
        phone_number = input("Nhập số điện thoại cần đăng kí: ")
        if phone_number.isdigit() and len(phone_number) == 10:
            break
        else:
            print("Số điện thoại phải chứa đúng 10 kí tự số.")

    for record in data:
        if record[0] == phone_number:
            print("Số điện thoại đã tồn tại, vui lòng đăng kí số khác")
            return add_record()

    name = input("Nhập họ và tên: ")
    address = input("Nhập địa chỉ: ")

    while True:
        gender = input("Nhập giới tính (Nam/Nu): ").lower()
        if gender in ['nam', 'nu']:
            break
        else:
            print("Giới tính chỉ được nhập Nam hoặc Nữ, không phân biệt chữ hoa thường.")

    while True:
        cccd = input("Nhập số CCCD (chỉ 12 kí tự số): ")
        if cccd.isdigit() and len(cccd) == 12:
            break
        else:
            print("CCCD phải chứa đúng 12 kí tự số.")

    data.append([phone_number, name, address, gender, cccd])
    write_data(data)
    print("Đã thêm đăng ký số điện thoại.")


def edit_record():
    data = read_data()
    phone_number = input("Nhập số điện thoại cần sửa: ")
    for record in data:
        if record[0] == phone_number:
            record[1] = input("Nhập họ và tên mới: ")
            record[2] = input("Nhập địa chỉ mới: ")
            record[3] = input("Nhập giới tính mới (Nam/Nữ): ")
            record[4] = input("Nhập số CCCD mới: ")
            write_data(data)
            print("Đã cập nhật thông tin.")
            return
    print("Không tìm thấy số điện thoại.")

def delete_record():
    data = read_data()
    phone_number = input("Nhập số điện thoại cần xoá: ")
    for record in data:
        if record[0] == phone_number:
            data.remove(record)
            write_data(data)
            print("Đã xoá đăng ký số điện thoại.")
            return
    print("Không tìm thấy số điện thoại.")

def view_by_prefix():
    prefix = input("Nhập đầu số cần xem: ")
    data = read_data()
    matching_records = [record for record in data if record[0].startswith(prefix)]
    if matching_records:
        print("Danh sách số điện thoại thuộc đầu số", prefix + ":")
        for record in matching_records:
            print(" - ".join(record))
        print("Tổng số lượng số điện thoại thuộc đầu số", prefix + ":", len(matching_records))
    else:
        print("Không có số điện thoại nào thuộc đầu số", prefix)

def view_raw_data():
    data = read_data()
    print("\033[1mDữ liệu thô trong file:\033[0m")
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

def main():
    while True:
        menu()
        choice = input("\033[1mNhập lựa chọn của bạn:\033[0m ")
        if choice == '1':
            add_record()
        elif choice == '2':
            edit_record()
        elif choice == '3':
            delete_record()
        elif choice == '4':
            view_by_prefix()
        elif choice == '5':
            view_raw_data()
        elif choice == '0':
            print("\033[1;31mCảm ơn bạn đã sử dụng chương trình. Tạm biệt và hẹn gặp lại!\033[0m")
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại....")

main()
