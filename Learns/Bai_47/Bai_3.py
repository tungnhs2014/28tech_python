'''
Tính tổng hàm S(n) = 1^3 + 2^3 + 3^3 + 4^3 + .. + n^3 bằng đệ quy. 
Nếu bạn chưa biết thì S(n) có thể tính nhanh bằng công thức S(n) = [(n * (n + 1) / 2)]^2

Input Format
Số nguyên dương n.

Constraints
0≤n≤10^3; Chú ý các bạn phải code bằng đệ quy nhé.

Output Format
In ra kết quả của S(n)

Sample Input 0
435

Sample Output 0
8992728900
'''

def tong(n):
    if n == 0:
        return 0
    return n ** 3 + tong(n-1)

if __name__ == '__main__':
    n = int(input())
    print(tong(n))