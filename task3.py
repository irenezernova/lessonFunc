def sum_digit(num):
    str_num = str(num)
    n = len(str_num)
    sum = 0
    for i in range(n):
        sum += int(str_num[i])
    return sum

print('input number: ')
a = int(input())
print("sum of digits =", sum_digit(a))
