'''
Tìm ước chung lớn nhất và bội chung nhỏ nhất của 2 số nguyên

Input Format
2 số nguyên a, b

Constraints
1≤a,b≤10^12

Output Format
Ước chung lớn nhất và bội chung nhỏ nhất, dữ liệu đảm bảo BCNN của 2 số không vượt quá số int 64bit

Sample Input 0
20 50

Sample Output 0
10 100
'''

def _gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(_gcd(a, b),  (a *b) // _gcd(a, b))