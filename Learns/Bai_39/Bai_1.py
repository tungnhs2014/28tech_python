'''
Kiểm tra một số nguyên không âm N có phải là số nguyên tố hay không?

Input Format
Dòng duy nhất chứa số nguyên dương N

Constraints
0≤N≤10^9

Output Format
In ra YES nếu n là số nguyên tố, ngược lại in NO.

Sample Input 0
999999999

Sample Output 0
NO

Sample Input 1
17

Sample Output 1
YES
'''

import math

def SNT(n):
    if n < 2:
        return False
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

#code
if __name__ == '__main__':
    n = int(input())
    if (SNT(n)):
        print('YES')
    else:
        print('NO')
