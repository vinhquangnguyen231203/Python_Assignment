while True:
    try:
        height = int(input('Nhập chiều cao(>=5): '))
        if(height<5):
           print('Chiều cao ko hợp lệ')
           continue
        for i in range(height):
            for j in range(height * 2):
                if j == i or j == height * 2 - i - 1:
                    print("*"*2, end="")
                else:
                    print(" ", end="")
            print()
    except:
        print('Vui lòng nhập số')
        continue