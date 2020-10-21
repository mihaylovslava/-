import random

N = random.randrange(1,10)
print('N = ', N)
A = random.randrange(-10,10)
print('A = ', A)

P = 1.0
S = 1.0
for i in range(1,N+1):
    P *= A
    S += P
    print(i," : ", P," : ", S)
print("Result:",S)