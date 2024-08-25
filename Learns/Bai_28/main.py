#Tính tổng ước và đếm ước của 1 số: Duyệt tới căn bậc 2 của n là đủ
import math

def dem_uoc(n):
    cnt = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            cnt += 1
            if i != n //i:
                cnt += 1
    return cnt

def tong_uoc(n):
    tong = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n //i:
                tong += n // i
    return tong

if __name__ == '__main__':
    n = int(input())
    print(dem_uoc(n)) 
    print(tong_uoc(n)) 
