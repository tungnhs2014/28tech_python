#Kiểm tra số nguyên tố
#Số nguyên tố: số nguyên dương, và chỉ có 2 ước là 1 và chính nó, (1 không phải là snt): 2, 3, 5, 7, 13, 17, 19...
#Lưu ý: Khi code kiểm tra tính chất đúng sai => Nên cố gắng kiểm tra nó sai => Kết luận luôn bằng câu lệnh return

import math
def prime(n):
    if n < 2: return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

#Liệt kê các số nguyên tố từ 1 đến n
def list_prime(n):
    for i in range(1, n + 1):
        if(prime(i)):
            print(i, end = ' ')

if __name__ == '__main__':
    n = int(input())
    if prime(n):
        print('YES')
    else:
        print('NO')
    list_prime(n)
