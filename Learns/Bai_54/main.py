#LIST
a = [1, 2, 3, 4, 5, '28 tech', 'python']
print(type(a))
print(a[0])
print(a[-1])

s = 'Son Tung' #iterable
b = list(s)
print(b)
print(len(b))

c = list(range(20))
print(c)

d = [1, 2, 3, 4, 5]
for i in range(0, len(d)): #0, 1, 2,..len - 1
    print(d[i], end = ' ')
print()
for i in range(len(d)-1, -1, -1):
    print(d[i], end = ' ')
    
print()
#for each
for item in d:
    print(item, end = ' ')

a[2] = "Son Tung"
print('\n',a)
a.append(10)
print(a)
#chen 100 vao vi tri so 2
a.insert(2, 100)
print(a)
#Xoa phan tu trong list
a.pop(2)
del a[1]
a.remove('Son Tung')
print(a)

#Sao chep list
e = a * 2
print(e)

#Tao list co 100 phan tu so 0
f = [0] * 100
print(f)

#Tim kiem trong list O(n):
if '28 tech' in a:
    print('YES')

#Combine list:
a += b
print(a)

c.extend(d)
c.sort() # O(nlogn) = Tim sort
print(c)

