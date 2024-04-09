dict_1 = {
    "CS101": "Introduction to Computer Science",
    "CS102": "Data Structures and Algorithms",
    "CS103": "Database Management Systems",
    "CS104": "Operating Systems",
    "CS105": "Software Engineering"
}

dict_2 = {
    "L1": "10A1",
    "L2": "10A2",
    "L3": "10A3",

}
dict_3 = dict_1.copy()
dict_3.update(dict_2)

print(dict_3)