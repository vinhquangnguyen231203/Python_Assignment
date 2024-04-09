
dict_1 = {
    "CS101": "Introduction to Computer Science",
    "CS102": "Data Structures and Algorithms",
    "CS103": "Database Management Systems",
    "CS104": "Operating Systems",
    "CS105": "Software Engineering"
}

key_to_remove = input('Nhập key cần xóa: ')

if(key_to_remove in dict_1):
    del(key_to_remove)
    print(f'Dict_1 sau khi xóa :{dict_1}')