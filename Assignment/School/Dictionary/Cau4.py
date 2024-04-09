Dict_2 = {
    "L1": "10A1",
    "L2": "10A2",
    "L3": "10A3",

}

# Thêm 2 lớp mới vào Dict_2
Dict_2["L4"] = "10A4"
Dict_2["L5"] = "10A5"

for lop,name in Dict_2.items():
    print(f'Mã Lớp: {lop}, Tên: {name}')