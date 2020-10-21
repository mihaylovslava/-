import random

N = random.randrange(1,10)
print("N = ",N)
r = False
for i in range(N):
    x = random.randrange(-10,10)
    r = (x>0)
    print(x," : positive - ",r)
    if r:
        break
print("There is a positive number:",r)