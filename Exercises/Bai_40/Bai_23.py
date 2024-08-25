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

def sum_digit(n):
    sum = 0
    for i in range(1, math.isqrt(n) + 1):
        if n % i == 0:
            sum += i
            if i != n // i:
                sum += n // i
    return sum

if __name__ == '__main__':
    n = int(input())
    print(sum_digit(n))
