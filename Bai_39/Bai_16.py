'''
Cho số tự nhiên N. Nhiệm vụ của bạn là hãy kiểm tra N có phải là số Smith hay không. 
Một số được gọi là số Smith nếu N không phải là số nguyên tố và có tổng các chữ số của N bằng tổng các chữ số của các thừa số nguyên tố trong phân tích của N. 
Ví dụ N = 666 có các thừa số nguyên tố là 2, 3, 3, 37 có tổng các chữ số là 18.

Input Format
Số nguyên dương N

Constraints
1≤N≤10^8.

Output Format
In ra YES nếu N là số Smith, ngược lại in ra NO.

Sample Input 0
22

Sample Output 0
YES
'''

from math import *

def sum_digit(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    return tong

def check(n):
    sum_1 = sum_digit(n)
    sum_2 = 0
    tmp = n
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while n % i == 0:
                sum_2 += sum_digit(i)
                n //= i
    if tmp == n:
        return False # N la SNT
    if n > 1:
        sum_2 += sum_digit(n)
    return sum_1 == sum_2

if __name__ == '__main__':
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')