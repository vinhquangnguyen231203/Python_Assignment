dict_1 = {
    "CS101": "Introduction to Computer Science",
    "CS102": "Data Structures and Algorithms",
    "CS103": "Database Management Systems",
    "CS104": "Operating Systems",
    "CS105": "Software Engineering"
}

value_to_remove = input("Nhập value muốn xóa: ")

keys_to_remove = [key for key, value in dict_1.items() if value == value_to_remove]
if keys_to_remove:
    for key in keys_to_remove:
        del dict_1[key]
    print("Dictionary sau khi xóa:")
    print(dict_1)
else:
    print("Value không tồn tại trong dictionary.")
