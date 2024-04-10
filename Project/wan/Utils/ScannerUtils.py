from Function.Read_File.Read_File import rwFile
import re

'''
Quy ước condition: phone,name,gender,address,cccd
'''
class ScannerUtils:

    @staticmethod
    def input_int(message):
        while True:
            try:
                return int(input(message))
            except ValueError:
                print("Vui long nhap so nguyen!")
    
    @staticmethod
    def input_str(message,condition):
        condition = condition.lower().strip()
        result = ''
        if(condition == 'phone'):
            result = ScannerUtils.input_phone_number(message)
        elif(condition == 'name'):
            result = ScannerUtils.input_fullName(message)
        elif(condition == 'gender'):
            result = ScannerUtils.input_gender(message)
        elif(condition == 'address'):
            result = ScannerUtils.input_address(message)
        elif(condition == 'cccd'):
            result = ScannerUtils.input_cccd(message)
        return result


    @staticmethod
    def input_phone_number(message,prefix):
        while True:
            try:
                numbs = int(input(message))
                if(ScannerUtils.validate_numbs(phone_number= numbs, numbs= 7)):
                    if(ScannerUtils.check_duplicate((str(prefix)+str(numbs).strip()))):
                        return str(prefix)+str(numbs).strip()
                    else:
                        print('Số điện thoại đã tồn tại !!')
                else:
                    print("Vui long nhap so dien thoai hop le!!")
            except ValueError:
                print("Vui lòng nhập số điện thoại")
    
    
    def validate_numbs(phone_number, numbs):
        pattern = r'[0-9]{%d}$' % numbs
        if re.match(pattern, str(phone_number)):
            return True
        return False
    
    
    

    def input_fullName(message):
        while True:
            try:
                fullName = input(message)

                ''' Kiểm tra'''
                if(len(fullName) == 0):
                    print('Không được để trống')
                    continue

                fullName = fullName.lower().strip().title()

                return fullName
            except ValueError:
                print("Vui lòng nhập chuỗi!!")
    
    def input_gender(message):
        while True:
            try:
                gender = input(message).lower().strip()
                
                if(gender == ''):
                    print('Khong duoc de trong!!')
                    continue
                if((gender == 'nam' or gender == 'n')):
                    return 'Nam'
                elif ((gender == 'nam' or gender == 'n') or gender == 'nữ'):
                    return 'Nữ'
                else:
                    print('Giới tính không hợp lệ')
                    continue
            except ValueError:
                print('Vui lòng nhập chuỗi!!')

    def input_cccd(message):
        while True:
            try:
                cccd = int(input(message))

                cccd = str(cccd).strip()

                if(len(cccd) == 0):
                    print('Không được để trống')
                    continue

                if(ScannerUtils.validate_numbs(cccd,10)):
                    return str(cccd)
                else:
                    print('Vui lòng nhập số CCCD hợp lệ!!')
                
            except ValueError:
                print("Vui long nhap so nguyen!!")
    
    def input_address(message):
        while True:
            try:
                address = input(message)

                ''' Kiểm tra'''
                if(len(address) == 0):
                    print('Không được để trống địa chỉ')
                    continue

                return address
            except ValueError:
                print("Vui long nhap chuoi!!")
    
    @staticmethod
    def input_prefix(result):
        while True:
            prefix = (input('Nhập đầu số: '))
            if(ScannerUtils.check_prefix(str(prefix),result)):
                return str(prefix)
            else:
                print('Đầu số không hợp lệ')
                continue

    def check_prefix(prefix,result):
        for prefix_list in result.values():
            if prefix in prefix_list:
                return True
        return False
    
    def check_duplicate(phone_number):
        data = rwFile.read_data()
        for numbs in data:
            if numbs[0] == phone_number:
                return False
        return True
    
    @staticmethod
    def input_edit_phone_number():
        while True:
            try:
                phone_number = int(input('Nhập số điện thoại cần thay đổi thông tin: '))
                phone_number = '0'+str(phone_number)

                ''' Kiểm tra đầu số có hợp lệ ko '''
                result = []
                print(type(result))
                result = ScannerUtils.check_prefix_edit_phone_number(phone_number= phone_number)
                if len(result) == 0:
                    print('Đầu số không hợp lệ')
                else:
                    return result
            except ValueError:
                print('Số điện thoại phải là số')

    def check_prefix_edit_phone_number(phone_number):
        data = rwFile.read_data()
        for datas in data:
            if datas[0] == phone_number:
                return datas
                            

                                
