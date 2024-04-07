print('CHƯƠNG TRÌNH VẼ CHỮ H')
while True:
    Cao = input('Nhập chiều cao (>=5): ').strip()
    if Cao=='': break
    if not Cao.isdigit():
        print('Xin nhập số')
        continue
    Cao=int(Cao)
    if Cao<5: continue
    Giua = Cao//2
    for i in range(Cao):
        print('\t', end='')
        for j in range(Cao):
            if i==Giua:
                print('@', end='')
            else:
                if j==0 or j==Cao-1:
                    print('@', end='')
                else:
                    print(' ', end='')
        print()
    print()

print('CHƯƠNG TRÌNH VẼ CHỮ E')
while True:
    Cao = input('Nhập chiều cao (>=5): ').strip()
    if Cao=='': break
    if not Cao.isdigit():
        print('Xin nhập số')
        continue
    Cao=int(Cao)
    if Cao<5: continue
    Giua = Cao//2
    for i in range(Cao):
        print('\t', end='')
        for j in range(Cao):
            if i==0 or i==Giua or i==Cao-1:
                print('@', end='')
            else:
                if j==0:
                    print('@', end='')
                else:
                    print(' ', end='')
        print()
    print()

print('CHƯƠNG TRÌNH VẼ CHỮ P')
while True:
    Cao = input('Nhập chiều cao (>=5): ').strip()
    if Cao=='': break
    if not Cao.isdigit():
        print('Xin nhập số')
        continue
    Cao=int(Cao)
    if Cao<5: continue
    Giua = Cao//2
    for i in range(Cao):
        print('\t', end='')
        for j in range(Cao):
            if i==0 or i==Giua:
                print('@', end='')
            elif Giua>i>0:
                if j==0 or j==Cao-1:
                    print('@', end='')
                else:
                    print(' ', end='')
            else:
                if j==0:
                    print('@', end='')
                else:
                    print(' ', end='')
        print()
    print()

print('CHƯƠNG TRÌNH VẼ CHỮ S')
while True:
    Cao = input('Nhập chiều cao (>=5): ').strip()
    if Cao=='': break
    if not Cao.isdigit():
        print('Xin nhập số')
        continue
    Cao=int(Cao)
    if Cao<5: continue
    Giua = Cao//2
    for i in range(Cao):
        print('\t', end='')
        for j in range(Cao):
            if i==0 or i==Giua or i==Cao-1:
                print('@', end='')
            elif Giua>i>0:
                if j==0:
                    print('@', end='')
                else:
                    print(' ', end='')
            else:
                if j==Cao-1:
                    print('@', end='')
                else:
                    print(' ', end='')
        print()
    print()

print('CHƯƠNG TRÌNH VẼ CHỮ Z')
while True:
    Cao = input('Nhập chiều cao (>=5): ').strip()
    if Cao=='': break
    if not Cao.isdigit():
        print('Xin nhập số')
        continue
    Cao=int(Cao)
    if Cao<5: continue
    for i in range(Cao):
        print('\t', end='')
        for j in range(Cao):
            if i==0 or i==Cao-1:
                print('@', end='')
            else:
                if j==Cao-1 -i:
                    print('@', end='')
                else:
                    print(' ', end='')
        print()
    print()
