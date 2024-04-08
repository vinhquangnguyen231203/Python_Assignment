'''
 ** Hàm count():
 - Công dụng: Đếm số lần xuất hiện của một phần tử
 trong danh sách
 - Cú pháp: Tên_List.count(Giá trị phần tử)
 
 ** Hàm extend():
 - Công dụng: Kế thừa các phần tử từ danh sách 2 và
 thêm vào danh sách 1
 - Cú pháp: Tên_List.extend(Tên_List2)

 ** Hàm index()
 - Công dụng: Tìm giá trị trong danh sách ( có phân biệt HOA
 thường). Nếu tìm thấy trả về một số (chỉ mục vị trí lần đầu 
 phát hiện được, nếu ko trả về biệt lệ)
 - Cú pháp: List_Mới = Tên_List.index(Giá trị)

 ** Hàm insert():
 - Công dụng: Chèn phần tử vào vị trí có chỉ mục được
 chỉ định
 - Cú pháp: Tên_List.insert(Chỉ mục, Giá trị phần tử)

 ** Hàm list():
 - Công dụng: Chuyển đổi kiểu dữ liệu của một biến sang
 dạng danh sách
 - Cú pháp : list(Tên_Biến)

 ** Hàm len():
 - Công dụng: Trả về số phần tử có trong danh sách
 - Cú pháp: len(Tên_List)

 ** Hàm max: Trả về phần tử lớn nhất ( nếu là số)
 Nếu là chuỗi trả về ký tự đầu lớn nhất
 Chỉ áp dụng cho List chứa 1 kiểu dữ liệu
 - Cú pháp : max(Tên_List)

 ** Hàm min: Trả về phần tử nhỏ nhất ( nếu là số)
 Nếu là chuỗi trả về ký tự đầu nhỏ nhất
 Áp dụng cho List chứa 1 kiểu dữ liệu

 ** Hàm pop(): Lấy ra khỏi danh sach phần tử
 tại vị trí có chỉ mục được chỉ định, nếu ko chỉ định
 vị trí thì mặc định là lấy phần tử cuối trong danh sách
 (giống như STACK)

 - Cú pháp : Tên_List.pop([Chỉ mục])

 ** Hàm reverse(): Đảo ngược các vị trí trong danh sách
 - Cú pháp : Tên_List.reverse()

 ** Hàm sort(): Sắp xếp lại danh sách theo một thứ tự xác 
 định
 - Cú pháp: Tên_List.sort([reverse = ...[, key = ....   ]])
 - Trong đó: reverse là một kiểu sắp xếp quy định
            + True: thì sắp giảm dần
            + False thì sắp tăng dần
            key: khóa dùng để sắp xếp, có thể là một hàm
'''