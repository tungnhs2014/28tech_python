a = [1, 2, 3, 4, 5]
b = a # a va b cung doi tuong, thao tac tren cung 1 dia dia
b[2] = 10
print(a)
print(b)
print(id(a))
print(id(b))

c = [1, 2, 3, 4, 5]
d = c.copy()
c[2] = 10
print(c)
print(d)
print(id(c))
print(id(d))