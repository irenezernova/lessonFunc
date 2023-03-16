def triang_check(a, b, c): #function that checks if 3 nums can be triangle sides
    if a+b>c and a+c>b and b+c>a:
        print("Треугольник!")
        return True
    else:
        print("Что-то непонятное")
        return False

def triang_square(a,b,c): #square with heron's formula
    if triang_check(a,b,c):
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**(0.5)
    else:
        return "это ты тогда сам считай"

def triang_perimeter(a,b,c):
    if triang_check(a,b,c):
        return a+b+c
    else:
        return "это ты тогда сам считай"

def rect_square(a,b):
    return a*b

def rect_perimeter(a,b):
    return 2*(a+b)

while True:
    print("Привет! Выбери тип фигуры: 1 - треугольник, 2 - прямоугольник, 0 - выйти из программы\n")
    ch1 = int(input()) #first choose in menu
    if ch1 == 0:
        print('ну ты заходи.. если что.')
        break
    elif ch1 != 1 and ch1 != 2:
        print("что-то не то, давай еще раз...")
        continue
    print("Отличный выбор! А что посчитать? 1 - периметр, 2 - площадь \n")
    ch2 = int(input())
    if ch1 == 1:
        print("Введи три стороны треугольника. Первая: ")
        a = int(input())
        print("Вторая: ")
        b = int(input())
        print("Третья: ")
        c = int(input())
        if ch2 == 1:
            print("P =", triang_perimeter(a,b,c))
        elif ch2 == 2:
            print("S =", triang_square(a,b,c))
        else:
            print("что-то не то, давай еще раз...")
            continue
    elif ch1 == 2:
        print("Введи две стороны прямоугольника. Первая: ")
        a = int(input())
        print("Вторая: ")
        b = int(input())
        if ch2 == 1:
            print("P =", rect_perimeter(a,b))
        elif ch2 == 2:
            print("S =", rect_square(a,b))
        else:
            print("что-то не то, давай еще раз...")
            continue

