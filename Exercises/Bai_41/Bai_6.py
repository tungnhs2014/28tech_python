'''
Một số được coi là thuần nguyên tố nếu nó là số nguyên tố, tất cả các chữ số là nguyên tố và tổng chữ số của nó cũng là một số nguyên tố.
Bài toán đặt ra là đếm xem trong một đoạn giữa hai số nguyên cho trước có bao nhiêu số thuần nguyên tố.

Input Format

Một dòng hai số nguyên dương tương ứng, cách nhau một khoảng trống.

Constraints

Các số đều không vượt quá 9 chữ số.

Output Format

Viết ra số lượng các số thuần nguyên tố tương ứng

Sample Input 0

2345 6789
Sample Output 0

15
'''

import math

def check_prime(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

def check(n):
    tong = 0
    while n != 0:
        r = n % 10
        if r != 2 and r != 3 and r != 5  and r != 7:
            return False
        tong += r
        n //= 10
    if not check_prime(tong):
        return False
    return True

if __name__ == '__main__':
    dem = 0
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if(check(i)) and check_prime(i):
            dem +=1
    print(dem)