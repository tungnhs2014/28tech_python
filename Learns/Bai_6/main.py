# a = input('Nhap chuoi str: ')
# b = int(input('Nhap chuoi nguyen: '))

# print(type(a))
# print(a)
# print(type(b))
# print(b)


# c = int(input('Nhap chieu rong: '))
# d = int(input('Nhap chieu dai: '))
# cv = 2 *(c + d)
# dt = c * d
# print(cv, dt)

#Buoc 1: nhap
s = input('Nhap 3 so: ')
#Buoc 2: Tach cac so ra
m = s.split()
#Buoc 3: Su dung map de ep cac phan tu trong list => sang kieu du lieu mong muon
x, y, z = map(int, m)
print(x + y + z)

#Nhap 4 so float tren 1 dong
a, b, c, d = map(float, input('Nhap 4 so thuc: ').split())
print(a  + b + c + d)