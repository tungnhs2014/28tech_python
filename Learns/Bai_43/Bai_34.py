'''
Cho 4 số nguyên dương x, y, z, n. Tìm số nguyên dương nhỏ nhất có n chữ số chia hết cho cả x, y, và z.

Input Format
4 số nguyên dương x, y, z, n

Constraints
(1 ≤x,y,z≤10^4); n≤16

Output Format
Kết quả của bài toán, trường hợp không tìm được số thỏa mãn in -1

Sample Input 0
2 3 5 4

Sample Output 0
1020

Sample Input 1
3 5 7 2

Sample Output 1
-1
'''

from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def lcm(a, b):
    return a  * b // gcd(a, b)

if __name__ == '__main__':
    x, y, z, n = map(int, input().split())
    bc = lcm(lcm(x, y), z)
    #Tim so nho nhat => 10 ** (n - 1) chia het cho bc
    tmp = 10 ** (n - 1)
    ans = (tmp + bc - 1) // bc * bc
    if ans < 10 ** n:
        print(ans)
    else:
        print(-1)