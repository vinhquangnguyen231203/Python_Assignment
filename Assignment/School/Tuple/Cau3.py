# Tạo một tuple với các phần tử bất kỳ
my_tuple = (1, 'hello', 3.14, True, [5, 6, 7])

# Phần tử cần kiểm tra vị trí
element = 3.14

# Tìm vị trí của phần tử trong tuple
position = my_tuple.index(element)

# In ra vị trí của phần tử
print(f"Phần tử {element} được tìm thấy ở vị trí thứ {position + 1} trong tuple.")
