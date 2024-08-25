'''
Tính tổng ước của 1 số nguyên dương N.

Input Format
1 số nguyên dương N

Constraints
1≤N≤10^12.

Output Format
Tổng ước số của N

Sample Input 0
100

Sample Output 0
217

Sample Input 1
28

Sample Output 1
56
'''

import math

def tong_uoc(n):
    tong = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            tong += i
            if i != n // i:
                tong += n // i
    return tong

#code
if __name__ == '__main__':
    n = int(input())
    print(tong_uoc(n))
