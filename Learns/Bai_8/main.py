#Kiểm tra số nằm trng đoạn [a, b]
#and or not
a, b = 120, 100
m = 60
if (m >= a) and (m <= b):
    print('YES')

#Kiểm tra số chẵn lẽ
n = 61
if n % 2 == 0:
    print(n, 'is even')
else:
    print(n, 'is old')

if a > b:  print(a, 'greater than', b); print("Son Tung"); print("MTP") #shortland if
elif a == b:
    print(a, 'eual to', b)
else:
    print(a, 'less than', b)

#Toán tử 3 ngôi
res = 'SOn TUng' if a < b else 'MTP'
print(res)

#if lồng nhau(nested if)
#Kiểm tra xem n có phải là số lơn hoặc bằng 50 và chia hết cho 1 trong 3 số 3 5 7

if n > 50:
    if n % 3 == 0 or n % 5 == 0 or n % 7 == 0:
        print('YES')
    else:
        print('NO')
else:
    print('NO')