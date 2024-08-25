'''
Kiểm tra một số nguyên có phải là số chính phương hay không? Định nghĩa số chính phương: 

Input Format
Một số nguyên dương N

Constraints
1≤N≤10^18

Output Format
In ra YES nếu N là số chính phương, ngược lại in NO

Sample Input 0
169

Sample Output 0
YES
'''
import math

def chinh_phuong(n):
    can = math.isqrt(n)
    if can ** 2 != n:
        return False
    return True

if __name__ == '__main__':
    n = int(input())
    if chinh_phuong(n):
        print('YES')
    else:
        print('NO')