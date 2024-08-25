from math import *

#O(can(n))
def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

#O(logN)
def tong(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

if __name__ == '__main__':
    n = int(input())
    for i in range(n + 1):
        if(nt(i)):
            print(i, end = ' ')