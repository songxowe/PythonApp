# 形参 Parameters
def print_max(a, b):
    if a > b:
        print(a, 'is maximum')
    elif a == b:
        print(a, 'is equal to', b)
    else:
        print(b, 'is maximum')


# 直接传递字面值 (实参 Arguments)
print_max(4, 3)
x = 5
y = 7
# 以参数的形式传递变量
print_max(x, y)
