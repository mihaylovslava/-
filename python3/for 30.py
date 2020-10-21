import random
import math

B = random.randrange(-9,11)
A = random.randrange(-10,B)
N = random.randrange(2,11)

H = (B - A) / N
print("A = ",A)
print("B = ",B)
print("N = ",N)
print("H = {0:.2f}".format(H))

x = A
for i in range(0,N+1):
    y = 1 - math.sin(x)
    print("{0:.2f} : {1:.4f}".format(x,y))
    x += H