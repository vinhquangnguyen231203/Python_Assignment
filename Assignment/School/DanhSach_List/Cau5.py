chuoi = input('Nhập vào chuỗi: ')

ds_ky_tu = []
ds_ky_tu_db = []
ds_ky_so = []

for c in (chuoi):
    if(c.isalpha()):
        ds_ky_tu.append(c)
    elif (c.isdigit()):
        ds_ky_so.append(c)
    else:
        ds_ky_tu_db.append(c)

print(f'Có {len(ds_ky_tu)}  ký tự: {ds_ky_tu}')
print(f'Có {len(ds_ky_so)} ký số: {ds_ky_so}')
print(f'Có {len(ds_ky_tu_db)} ký tự đặc biệt: {ds_ky_tu_db}')