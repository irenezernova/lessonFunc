def triang_check(a, b, c):
    if a+b>c and a+c>b and b+c>a:
        print("Треугольник!")
        return True
    else:
        print("Что-то непонятное")
        return False

def triang_square(a,b,c):
    if triang_check(a,b,c):
        p = (a+b+c)/2
        return (p*(p-a)*(p-b)*(p-c))**(0.5)

def triang_perimeter(a,b,c):
    if triang_check(a,b,c):
        return a+b+c

def rect_square(a,b):
    return a*b

def rect_perimeter(a,b):
    return 2*(a+b)

print("Привет! Выбери тип фигуры: 1 - треугольник, 2 - прямоугольник\n")


