'''
Tính n giai thừa bằng đệ quy.

Input Format
Số nguyên dương N.

Constraints
0≤n≤10;

Output Format
Kết quả của N!

Sample Input 0
6

Sample Output 0
720
'''

def tong(n):
    if n == 0 or n == 1:
        return 1
    return n * tong(n -1)

if __name__ == '__main__':
    n = int(input())
    print(tong(n))