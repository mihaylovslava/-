import random

A = random.randrange(1,100)
B = random.randrange(1,A)
print("A = ", A)
print("B = ", B)
x = int(A/B)
print("Количество полных B в A: ", x)