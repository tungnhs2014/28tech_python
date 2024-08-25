a = [1, 2, 3, 4, 5 ,6, 7, 8]
b = []
for x in a:
    if x % 2 == 0:
        b.append(x)
print(b)

c = [x ** 2 for x in a]
print(c)

d = [x ** 2 for x in range(1, 11)]
print(d)

def digit_sum(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

e = [1, 234, 32, 4, 55, 546, 12, 123]
f = [digit_sum(x) for x in e]
print(f)

g = [x for x in a if x % 2 ==0]
print(g)