def draw_N(height):
    # Vẽ phần đầu của chữ N
    for i in range(height):
        print("*", end="")
        for j in range(height):
            if j == height - 1 or i == j:
                print("*", end="")
            else:
                print(" ", end="")
        print()

    # Vẽ cột thẳng dưới của chữ N
    for i in range(height):
        print("*", end="")
        for j in range(height):
            if j == 0 or j == height - 1:
                print("*", end="")
            else:
                print(" ", end="")
        print()

# Nhập chiều cao từ người dùng
height = int(input("Nhập chiều cao của chữ N: "))

# Vẽ chữ N với chiều cao đã nhập
draw_N(height)
