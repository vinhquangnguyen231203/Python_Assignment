while True:
    try:
        print('------------GIẢI PT BẬC 2-------------') 
        a = float(input('a = '))
        b = float(input('b = '))
        c = float(input('c = '))
        if (a == 0):
            if (b == 0):
                if (c == 0):
                    print('Phuong trinh co vo so nghiem')
                else:
                    print('Phuong trinh vo nghiem')
            else:
                print('Phuong trinh co nghiem duy nhat: ', -c/b)
        else:
            delta = b*b - 4*a*c
            if (delta < 0):
                print('Phuong trinh vo nghiem')
            elif (delta == 0):
                print('Phuong trinh co nghiem kep: ', -b/(2*a))
            else:
                print('Phuong trinh co 2 nghiem phan biet: ', (-b + delta**0.5)/(2*a), 'va', (-b - delta**0.5)/(2*a))
        break

    except ValueError:
        print('Vui long nhap so thuc')