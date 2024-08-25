'''
Tính tổng hàm S(n) = 1^2 + 2^2 + 3^2 + 4^2 + .. + n^2 bằng đệ quy. 
Nếu bạn chưa biết thì S(n) có thể tính nhanh bằng công thức S(n) = n * (n + 1) * (2n + 1) / 6

Input Format
Số nguyên dương n.

Constraints
0≤n≤1000; Chú ý các bạn phải code bằng đệ quy nhé.

Output Format
In ra kết quả của S(n)

Sample Input 0
53

Sample Output 0
51039
'''

def tong(n):
    if n == 0:
        return 0
    return n ** 2 + tong(n-1)

if __name__ == '__main__':
    n = int(input())
    print(tong(n))