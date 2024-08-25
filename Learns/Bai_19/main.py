#range
#break, continue
#nested loop: Vòng lặp for lồng nhau

a = range(1, 10)
for i in a:
    print(i, end = ' ')
print()
n = 15
for i in range(n, 0, -1):
    print(i, end = ' ')

print()

for i in range(1, 7):
    print(i)
    i += 10
    print(i)
else:
    print('Vong lap da ket thuc')

for i in range(1, 27):
    print(i, end = ' ')
    if i % 7 == 0:
        break
    print('Cau lenh ben duoi break')

for i in range(1, 10):
    print("Son Tung")
    continue
    print("MTP")

for i in range(3):
    for j in range(2):
        print(i, j)