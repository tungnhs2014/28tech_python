'''
Tìm ước số nguyên tố lớn nhất của một số nguyên dương.

Input Format
Dòng đầu tiên là số lượng test case T; T dòng tiếp theo mỗi dòng là một số nguyên dương N

Constraints
1≤T≤500; 2≤N≤10000000

Output Format
Ước số nguyên tố lớn nhất của n in ra mỗi test case trên 1 dòng

Sample Input 0
2
10
17

Sample Output 0
5
17
'''

from math import *

def solve(n):
    ans = -1
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            ans = i
            while n % i == 0:
                n //= i
    if n > 1:
        ans = n
    return ans

if __name__ == '__main__':
    TC = int(input())
    for i in range(TC):
        n = int(input())
        print(solve(n))