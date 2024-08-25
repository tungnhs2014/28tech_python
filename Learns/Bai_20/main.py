n = 1
while(n <=5):
    print(n)
    n += 1
else:
    print('Vong lap while ket thuc khi n =', n)

a, b = 10, 20
while a <= b:
    print(a)
    a += 1
    continue
    print("Son Tung")

#Yêu cầu nhập số dương, nhập số âm, hoặc số 0 thì bắt nhập lại
# while True:
#     n = int(input())
#     if n > 0:
#         break

print()
#Chữ số của 1 số nguyên
#Tính tổng chữ số, đếm chữ số, tính tổng chữ số chẵn, chữ số lẻ, chữ số nguyên tố, số thuận nghịch, số thuận nghịch,...

n = 1234
dem = 0
tong = 0
lat = 0
while(n != 0):
    dem +=1
    tong += n % 10
    lat = lat * 10 + n % 10
    n //= 10
print('Chu so cua chua so n la', dem)
print('Tong so cua chua so n la', tong)
print('So thuat nghich cua n la', lat)


