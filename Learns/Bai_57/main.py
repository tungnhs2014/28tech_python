
func = lambda x : 2 *x #co tham so la x va tra ve la 2x
print(func(10))
print((lambda x : x ** 3)(2))


func1 = lambda x, y, z : x + y + z
print(func1(100, 200, 300))
print((lambda x, y, z : x + y + z)(100, 200, 300))

a = [1, -2, -3, 4, -5]
b = list(map(lambda x : x ** 2, a))
print(b)

c = list(filter(lambda x : x > 0, a))
print(c)

findmax = lambda x, y : x if x > y else y
print(findmax(2, 4))