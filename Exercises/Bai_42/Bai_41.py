'''
Một số được coi là đẹp nếu chữ số đầu gấp đôi chữ số cuối hoặc ngược lại; 
đồng thời các chữ số từ vị trí thứ 2 đến gần cuối thỏa mãn là một số thuận nghịch. 
Ví dụ: các số 36788766; 12345654322 là các số đẹp. Viết chương trình kiểm tra số đẹp theo tiêu chí trên.

Input Format
Số nguyên dương n

Constraints
99≤n≤10^18

Output Format
Ghi ra YES tương ứng với số đẹp, NO trong trường hợp ngược lại

Sample Input 0
122222

Sample Output 0
YES
'''

from math import *

def tn(n):
    tmp = n
    rev = 0
    while n != 0:
        rev = rev * 10 + n % 10
        n //= 10
    return rev == tmp

def check(n):
    last = n % 10
    m = 0
    n //= 10
    while n >= 10:
        m = m * 10 + n % 10
        n //= 10
    return ((n * 2 == last) or (last * 2 == n)) and tn(m)

if __name__ == '__main__':
    n = int(input())
    if (check(n)):
        print('YES')
    else:
        print('NO')