s1 = 'wan'
s2 = 'ăn,ngủ,đi học'



# Chia chuỗi s2 thành một danh sách các từ và sử dụng join để ghép lại với khoảng trắng
s2 = ', '.join([s1 + ' ' + tu for tu in s2.split(',')])
print(s2)




