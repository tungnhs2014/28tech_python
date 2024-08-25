a = 100
b = a
aa, sb = 1.5, '28tech'
print(a, b)
print(aa, sb)

c, d = 2, 5
c, d = d, c
print(c, d)

#Toán tử toán hoc
tong = c + d
hieu = c - d
tich = c * d
thuong_1 = c / d # chia lấy cả phần thập phân
thuong_2 = c // d # chia lấy phần nguyên
du = c % d
tmp = c ** d # tmp = c ^ d
print(tong, hieu, tich, thuong_1, thuong_2, du, tmp)

#Toán từ so sánh
print(100 == 100)
print(100 != 100)
print(100 > 100)
print(100 >= 120)
print(100 <= 150)

#Toán tử logic
print(20 == 20 and 10 == 10) #and
print(20 == 20 or 10 != 10) #or
print(not(10 == 10)) #not

#Toán tử nhận dạng
k = [1, 2, 3]
l = [1, 2, 3]
print(k is l)
print(k is not l)

#Toán tử thành viên

chuoi = 'Son Tung MTP'
print('MTP' in chuoi)
print('TungMTP' not in chuoi)


R = 15
chuvi = 2 * 3.14 * R
dientich = 3.14 * R * R
print('Chu vi hinh tron la: ', '%.2f' %chuvi)
print('Dien tich hinh tron la: ', '{:.2f}' .format(dientich))

print('Chu vi la: ', '%.2f' %chuvi)






