'''
Một số được coi là số đẹp khi nếu nó chia hết cho một số nguyên tố nào đó thì cũng phải chia hết cho bình phương của số nguyên tố đó.
Viết chương trình liệt kê các số đẹp như vậy trong đoạn giữa hai số nguyên dương cho trước

Input Format
2 số nguyên dương a, b

Constraints
1≤a≤b≤10^6

Output Format
In ra các số đẹp trong đoạn từ a tới b

Sample Input 0
3 49

Sample Output 0
4 8 9 16 25 27 32 36 49
'''
from math import *

def check(n):
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            dem = 0
            while n % i == 0:
                dem += 1
                n //= i
            if dem == 1:
                return False
    if n != 1:
        return False
    return True

if __name__ == '__main__':
    n, k = map(int, input().split())
    for i in range(n, k + 1):
        if check(i):
            print(i, end = ' ')