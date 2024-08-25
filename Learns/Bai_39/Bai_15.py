'''
Số nguyên dương N được gọi là số Sphenic nếu N được phân tích duy nhất dưới dạng tích của ba thừa số nguyên tố khác nhau. 
Ví dụ N=30 là số Sphenic vì 30 = 2×3×5; N = 60 không phải số Sphenic vì 60 = 2×2×3×5. Cho số tự nhiên N, nhiệm vụ của bạn là kiểm tra xem N có phải số Sphenic hay không?

Input Format
Một số nguyên dương N

Constraints
1≤N≤10^18

Output Format
Đưa ra 1 hoặc 0 tương ứng với N là số Sphenic hoặc không.

Sample Input 0
999923001838986077

Sample Output 0
1

Sample Input 1
30

Sample Output 1
1
'''

from math import *

def sphenic(n):
    cnt = 0
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            mu = 0
            while n % i == 0:
                mu += i
                n //= i
            if mu >= 2:
                return False
            cnt += 1
    if n > 1:
        cnt += 1
    return cnt == 3

if __name__ == '__main__':
    n = int(input())
    if sphenic(n):
        print('1')
    else:
        print('0')