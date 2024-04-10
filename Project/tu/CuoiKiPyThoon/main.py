import sys
from model import add_record,edit_record,delete_record,view_by_prefix,view_raw_data,menu
      
def main():
    menu()
    while True:
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
            print("\033[1;37mCảm ơn bạn đã sử dụng chương trình. Tạm biệt và hẹn gặp lại!\033[0m")
            print("\n")
            break
        else:
            print("\033[1;31mLựa chọn không hợp lệ. Vui lòng chọn lại....\033[0m")
            print("\n")
            
            
main()
