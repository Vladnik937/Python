# Ex 1
def f(x):
    return x ** 2


result = f(4)
print(result)


# Ex 2
def f(x):
    print(x)


f("string")


# Ex 3
def params(x, y, z, p=2, i=1):
    return x + y + z + p + i


result = params(1, 2, 3)
print(result)


# Ex 4
def first(x):
    return x / 2


def second(x):
    return x * 4


per = first(8)
per2 = second(per)
print(per2)


# Ex 5
a = input("Введите число")
def st(a):
    try:
        return float(a)
    except ValueError:
        print("Не удалось преобразовать строку в число с плавающей точкой.")


print(st(a))