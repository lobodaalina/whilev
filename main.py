a = int(input("Введите значение А"))
b = int(input("Введите значение B"))
c = int(input("Введите значение C"))


def func(a, b, c):
    while a < b:
        print(a, "Пока что нет")
        a = a + c
    else:
        print("Дождались!", a, "!")


func(a, b, c)
