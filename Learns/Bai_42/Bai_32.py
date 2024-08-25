'''
Đưa ra số nguyên tố thứ k trong phân tích thừa số nguyên tố của một số nguyên dương n. Ví dụ n=28, k=3 ta có kết quả là 7 vì 28=2x2x7.

Input Format
2 số n,k

Constraints
1 ≤n,k≤10^9

Output Format
In ra thừa số nguyên tố thứ k của n, nếu n không có thừa số nguyên tố thứ k thì in ra -1.

Sample Input 0
28 3

Sample Output 0
7

Sample Input 1
8 5

Sample Output 1
-1
'''

from math import *

def solve(n, k):
    dem = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            while(n % i == 0):
                dem +=1
                if dem == k:
                    return i
                n //= i
    if n != 1:
        dem +=1
    if dem == k:
        return n
    return -1

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(solve(n, k))


