#Số hoàn hảo
#28 = 1 + 2 + 4 +7 + 14

from math import *

def perfect(n):
    tong = 1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong == n

def prime(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

#Định lý Ecuild-Euler
#Nếu p là số nguyên tố và 2^p - 1 cũng là số nguyên tố =>(2^p -1) * 2^(p-1)=> Số hoàn hả

def perfect_2(n):
    for p in range(2, 33):
        if prime(p):
            if(prime(2 ** p -1 )):
                print('So fibonaci thu', (2 ** p - 1) * 2 **(p -1))
                if(2 ** p - 1) * 2 ** (p -1) == n:
                    return True
    return False

#code
if __name__ == '__main__':
    n = int(input())
    print(perfect_2(n))