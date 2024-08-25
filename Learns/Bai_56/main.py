# a[start, stop, step]
a = [10, 20, 30, 40, 50, 60]
b = a[2:6:1]
c = a[::-1]
print(b)
print(c)

#Thay doi gia tri cua list
a[2:5] = [100 , 200 ,300]
print(a)
#Xoa list
a[2:4] = []
print(a)
#Chen vao dau list
a[:0] = [1, 2, 3]
print(a)
#Chen vao cuoi list
a[len(a):] = [4, 5, 6]
print(a)

#Shadow copy
e = a[::]
print(e)
print(a == e)
print(a is e)