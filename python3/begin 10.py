import random

a = random.randrange(1,10)
b = random.randrange(1,10)
print("a = ", a)
print("b = ", b)
a2 = a**2
b2 = b**2
print("Квадрат a = ", a2)
print("Квадрат b = ", b2)
print("Сумма квадратов: ", a2+b2)
print("Разность квадратов: ", abs(a2-b2))
print("Произведение квадратов: ", a2*b2)
print("Частное квадратов: ", a2/b2)
