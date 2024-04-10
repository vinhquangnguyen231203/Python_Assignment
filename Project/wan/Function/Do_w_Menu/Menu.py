from Utils.ScannerUtils import ScannerUtils
from model.Provider_Data import providers
from model.Customer import Customer
from model.PhoneNumber import PhoneNumber
from Function.Read_File.Read_File import rwFile


def menu():
    ''' Hàm hiển thị các tùy chọn menu '''
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

def main():
    ''' Chương trình chính '''
    while True:
        menu()
        choice = ScannerUtils.input_int("\033[1mNhập lựa chọn của bạn:\033[0m ")
        if choice == 0:
            exit_program()
        elif choice == 1:
            add_record()
        elif choice == 2:
            edit_record()
        elif choice == 3:
            delete_record()
        elif choice == 4:
            pass
        elif choice == 5:
            pass
        else:
            print("\033[1mLựa chọn ko tồn tại - vui lòng nhập lại:\033[0m ")
            continue


def choose_network():
    '''Chọn nhà mạng cần đăng ký'''
    print("+" + "-"*66 + "+")
    print("|" + " "*66 + "|")
    print("|\033[1;32m" + "Chọn nhà mạng cần đăng ký:" + " "*23 + "\033[0m|")
    print("|" + " "*66 + "|")
    print("+" + "-"*66 + "+")
    print("|" + " "*66 + "|")
    print("|\033[1;34m 1: Mobifone" + " "*41 + "\033[0m|")
    print("|\033[1;34m 2: Vinafone" + " "*50 + "\033[0m|")
    print("|\033[1;34m 3: Viettel" + " "*45 + "\033[0m|")
    print("+" + "-"*66 + "+")
    
    result = {}
    while True:
        choice = ScannerUtils.input_int('Chọn nhà mạng cần đăng ký (1/2/3): ')
        if choice == 1:
            result = show_network("Mobifone")
            break
        elif choice == 2:
            result = show_network("Vinafone")
            break
        elif choice == 3:
            result = show_network("Viettel")
            break
        else:
            print('Vui lòng chọn nhà mạng cần đăng ký (1/2/3)!')
            continue
    
    return result

def show_network(network):
    ''' Hiển thị thông tin nhà mạng đã chọn '''
    print("+" + "-"*66 + "+")
    if network in providers:
        print(f"|\033[1;32m Thông tin nhà mạng {network}: \033[0m")
        print("+" + "-"*66 + "+")
        print("|\033[1;34m Đầu số: \033[0m", ", ".join(providers[network]))
        print("+" + "-"*66 + "+")
        return {network: providers[network]}
    else:
        print("|\033[1;31m Không tìm thấy thông tin cho nhà mạng", network, "\033[0m")
        print("+" + "-"*66 + "+")


def exit_program():
    ''' Thoát chương trình '''
    choice = input('Bạn có muốn thoát chương trình không (y/n): ')
    choice = choice.strip().lower()
    if (choice == 'y' or choice == 'yes'):
        print("\033[1;31m" + "Đã thoát khỏi chương trình" + "\033[0m")
        exit()

def add_record():
    ''' Đăng ký số điện thoại'''
    result = choose_network()
    prefix = ScannerUtils.input_prefix(result)
    numbs = ScannerUtils.input_phone_number(f'Nhập số điện thoại {prefix} (7 chữ số) : ', prefix)
    fullName = ScannerUtils.input_str(f'Nhập họ và tên: ', 'name')
    cccd = ScannerUtils.input_str(f'Nhập căn cước công dân: ', 'cccd')
    gender = ScannerUtils.input_str(f'Nhập giới tính: ', 'gender')
    address = ScannerUtils.input_str(f'Nhập địa chỉ: ', 'address')

    customer = Customer(id_customer= cccd, name= fullName, address= address, gender= gender)
    phone_numbers = PhoneNumber(provider= next(iter(result)), customer= customer, number= numbs)
    
    print('Đăng ký số điện thoại thành công!')

    data = rwFile.read_data()
    data.append([phone_numbers.toString()])
    rwFile.write_data(data= data)
    
def edit_record():
    ''' Sửa thông tin'''
    edit_phone()

def edit_phone():
    '''Input phone number need to edit in here'''
    phone_number = ScannerUtils.input_edit_phone_number()

    print(phone_number)

    phone = phone_number[0]
    provider = phone_number[1]
    details = phone_number[2]
    
    details = details.strip('[]')
    details = details.split(',+')

    # Truy cập các phần tử trong phần tử details
    id_number = details[:0]
    name = details[:0:1]
    address = details[::-1]


    # In ra thông tin đã truy cập
    print("Số điện thoại:", phone)
    print("Nhà mạng:", provider)
    print("ID:", id_number)
    print("Tên:", name)
    print("Địa chỉ:", address)


    # print("+" + "-"*66 + "+")
    # print("|" + " "*66 + "|")
    # print("|\033[1;32m" + f"Thông tin thuê bao {phone_number[1]}" + " "*23 + "\033[0m|")
    # print("|" + " "*66 + "|")
    # print("+" + "-"*66 + "+")
    # print("|" + " "*66 + "|")
    # print("|\033[1;34m [CCCD]: Căn cước công dân: " + f"{phone_number[2][0]}" + " "*41 + "\033[0m|")
    # print("|\033[1;34m [Name][2]: Tên Khách Hàng: " + f"{phone_number[2][1]}" +" "*50 + "\033[0m|")
    # print("|\033[1;34m [Address][3]: Địa chỉ: " + f'{phone_number[2][2]}' + " "*45 + "\033[0m|")
    #  # print("|\033[1;34m [Gender][4]: Giới tính: " + f'{phone_number[2][3]}' + " "*45 + "\033[0m|")
    # print("+" + "-"*66 + "+")

def delete_record():
    ''' Xoá số điện thoại'''
    pass


