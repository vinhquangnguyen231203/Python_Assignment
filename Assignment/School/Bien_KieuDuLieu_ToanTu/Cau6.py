while True:
    c = input('Nhập vào chuỗi')
    check = 'Chuỗi số' 
    for i in c:
        if(i.isalpha()):
            check = 'Chuỗi thường'
            break
    break
print(f'Đây là chuỗi: {check}')