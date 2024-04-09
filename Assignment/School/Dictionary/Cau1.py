# Dictionary biểu diễn 5 môn học cùng với mã môn học
dict_1 = {
    "CS101": "Introduction to Computer Science",
    "CS102": "Data Structures and Algorithms",
    "CS103": "Database Management Systems",
    "CS104": "Operating Systems",
    "CS105": "Software Engineering"
}

# In ra tất cả các môn học cùng với mã môn học
for course_code, course_name in dict_1.items():
    print(f"Mã môn học: {course_code} - Tên môn học: {course_name}")
