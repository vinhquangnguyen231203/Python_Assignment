# Tạo một tuple ban đầu
my_tuple = (1, 'hello', 3.14, True, [5, 6, 7])

# Giá trị mới cần thêm vào
new_value = 'world'

# Tạo một tuple mới bằng cách kết hợp tuple ban đầu và giá trị mới
new_tuple = my_tuple + (new_value,)

# In ra tuple mới
print(new_tuple)
