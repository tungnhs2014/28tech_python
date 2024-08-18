'''
Hãy phân tích một số nguyên dương N thành thừa số nguyên tố

Input Format
Số nguyên dương N

Constraints
2≤N≤10^16

Output Format
Phân tích thừa số nguyên tố của N, xem ví dụ để rõ hơn format.

Sample Input 0
60

Sample Output 0
2^2 * 3^1 * 5^1
'''

from math import *

def prime(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu +=1
                n //= i
            print(i, mu, sep = '^', end = '')
            if n !=1: # chua phan tich xong
                print(' * ', end = '')
    if(n > 1):
        print(n, 1, sep = '^')

if __name__ == '__main__':
    n = int(input())
    prime(n)