a = 100
b = 'Son Tung'
c = 10.45
A = 30
cp = 100 - 50j

# Trong python có thể xử lí số nguyên lớn, không giới hạn về giá trị mà số nguyên lưu
max = 1321423423423423423423423423423467547

print('Kieu du lieu cac bien: ', type(a), type(b), type(c))
print('Kieu du lieu cua bien cp: ', type(cp))

print(a, A)
print(max)

#Hệ nhị phân
x = 0b1101
#Hệ bát phân
y = 0o123
#Hệ thập lục phân
z = 0x22A

print(x, y, z)

aa = 3.5
print(aa)
bb = 3e5 # 3*10^5
print(bb)
cc = 1.9e308 # lớn hơn 1.8*10^308 => in ra inf(infinity)
print(cc)
dd = 5.4e-325 # nhỏ hơn 5*10^-324 => in ra 0
print(dd)

ee = 28.4356453
print('%.2f' %ee)
print(round(ee, 3))
print('{:.3f}' .format(ee))

# Số phức
ff = 3 + 5j
print(ff.real) # phần thực
print(ff.imag) # phần ảo

#bool
print(bool(100))
print(bool(0))
print(bool("Son Tung"))
print(bool(''))

#Casting (ép kiểu)
s = '42243'
ss = '''
4323.5454
'''
cas_1 = int(s)
cas_2 = float(ss)
cas_3 = str("22434")
print(cas_1, cas_2, sep = '\t', end = '\n')
print(type(cas_3))

