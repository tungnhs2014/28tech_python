'''
Một số được coi là số đẹp khi nó đồng thời vừa chia hết cho một số nguyên tố và chia hết cho bình phương của số nguyên tố đó. 
Viết chương trình liệt kê các số đẹp như vậy trong đoạn giữa hai số nguyên dương cho trước.

Input Format
2 số nguyên dương a, b

Constraints
1≤a≤b≤10^6

Output Format
In ra các số đẹp trong đoạn từ a tới b

Sample Input 0
4 50

Sample Output 0
4 8 9 12 16 18 20 24 25 27 28 32 36 40 44 45 48 49 50
'''

from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                dem += 1
                n //= i
            if dem >= 2:
                return True
    return False

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if check(i):
            print(i, end = ' ')