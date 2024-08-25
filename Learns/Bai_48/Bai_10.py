'''
Tính tổng S(n) = 1/1 + 1/2 + 1/3 + ... + 1/n bằng đệ quy.

Input Format
Số nguyên dương n.

Constraints
1≤n≤1000;

Output Format
In ra S(n) lấy 3 số sau dấu phẩy.

Sample Input 0
18

Sample Output 0
3.495
'''

def tong(n):
    if n == 0:
        return 0
    return 1 / n + tong(n -1)

if __name__ == '__main__':
    n = int(input())
    print('%.3f' %tong(n))