'''
Một số được coi là đẹp nếu nó là số thuận nghịch và có ít nhất 3 ước số nguyên tố khác nhau. 
Viết chương trình in ra các số đẹp như vậy trong một đoạn giữa hai số nguyên cho trước

Input Format
2 số a, b

Constraints
1≤a≤b≤10^7

Output Format
In ra các số đẹp trong đoạn a, b. Trong trường hợp không tồn tại số đẹp nào thì in ra -1.

Sample Input 0
1 1000

Sample Output 0
66 222 252 282 414 434 444 474 494 525 555 585 595 606 616 636 646 666 696 777 828 858 868 888 969
'''

from math import *

def tn(n):
    tmp = n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

def check(n):
    dem = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            dem += 1
            while n % i == 0:
                n //= i
    if n != 1:
        dem += 1
    return dem >= 3
#code
if __name__ == '__main__':
    a, b = map(int, input().split())
    dem = 0
    for i in range(a, b + 1):
        if tn(i) and check(i):
            print(i, end = ' ')
            dem +=1
    if dem == 0:
        print(-1)