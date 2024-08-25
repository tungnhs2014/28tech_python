'''
Liệt kê những số là số nguyên tố nhỏ hơn N và có tổng các chữ số của nó là một số trong dãy số Fibonacci.

Input Format
Dòng duy nhất chứa số nguyên dương N

Constraints
1<=N<=10000

Output Format
In ra các số nhỏ hơn N là số nguyên tố và thỏa mãn tổng chữ số của nó là một số trong dãy Fibonacci. Các số in cách nhau một khoảng trắng

Sample Input 0
114

Sample Output 0
2 3 5 11 17 23 41 53 67 71 101 107 113 
'''


from math import *

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check_fibo(n):
    if n == 1:
        return True
    fn1, fn2 = 1, 1
    for i in range(2, 20):
        fn = fn1 + fn2
        if fn == n:
            return True
        fn2, fn1 = fn1, fn
    return False

def tong(n):
    s = 0
    while n != 0:
        s += n % 10
        n //= 10
    return s

if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        if nt(i) and check_fibo(tong(i)):
            print(i, end = ' ')