'''
Cho 2 số a và b, hãy tính ước chung lớn nhất và bội chung nhỏ nhất của 2 số a và b. Trong đó hàm UCLN sử dụng đệ quy để tính.

Input Format
2 số nguyên dương a và b.

Constraints
1≤a,b≤10^12;

Output Format
In ra UCLN và BCNN của 2 số. Dữ liệu đảm bảo UCLN của 2 số nằm trong khoảng số nguyên 64 bit.

Sample Input 0
10 20

Sample Output 0
10 20
'''
def _gcd(a, b):
    if b == 0:
        return a
    return _gcd(b, a % b)

if __name__ == '__main__':
    a, b= map(int, input().split())
    print(_gcd(a, b), a * b // _gcd(a, b))
