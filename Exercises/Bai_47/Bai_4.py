'''
Tính tổng hàm S(n) = -1 + 2 -3 + 4 - 5 + 6 + ... + (-1)^n * n bằng đệ quy. 
Nếu bạn chưa biết thì S(n) có thể tính nhanh bằng công thức Nếu N chẵn thì S(n) = n / 2, còn nếu N lẻ thì S(n) = (n - 1) / 2 - n

Input Forma
Số nguyên dương n.

Constraints
1≤n≤10^3; Chú ý các bạn phải code bằng đệ quy nhé.

Output Format
In ra kết quả của S(n)

Sample Input 0
919

Sample Output 0
-460
'''


def tong(n):
    if n == 0:
        return 0
    else:
        if n % 2 == 0:
            return n + tong(n - 1)
        else:
            return -n + tong(n - 1)

if __name__ == '__main__':
    n = int(input())
    print(tong(n))