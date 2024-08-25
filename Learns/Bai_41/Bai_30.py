'''
Viết chương trình cho phép nhập vào n và liệt kê các số nguyên tố thỏa mãn nhỏ hơn hoặc bằng n và có chữ số cuối cùng lớn nhất. Có bao nhiêu số như vậy?

Input Format
Số nguyên dương n

Constraints
1≤n≤10^7

Output Format
Dòng đầu tiên liệt kê các số thỏa mãn, và dòng thứ 2 in ra số lượng số thỏa mãn.

Sample Input 0
200

Sample Output 0
2 3 5 7 11 13 17 19 23 29 37 47 59 67 79 89 101 103 107 109 113 127 137 139 149 157 167 179 199
29
'''

from math import *

def check(n):
    donvi = n % 10
    while n != 0:
        if n % 10 > donvi:
            return False
        n //= 10
    return True

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

#code
if __name__ == '__main__':
    n = int(input())
    dem = 0
    for i in range(n + 1):
        if check(i) and nt(i):
            print(i, end = ' ')
            dem += 1
    print('\n', dem, sep = '')