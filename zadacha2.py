import random

a = []
for i in range(5):
    a.append(random.randint(1, 10))
print(a)

b = []
for i in range(len(a) - 1):
    b.append(a[i])
    b.append(a[i] + a[i + 1])
b.append(a[-1])
print(b)
