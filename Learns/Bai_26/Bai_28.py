'''
Tính tổng S(n) = 1 + 1.2 + 1.2.3 + 1.2.3.4 + ... + 1.2.3....n

Input Format
Số nguyên dương n

Constraints
1<=n<=12

Output Format
In ra kết quả của S(n)

Sample Input 0
5

Sample Output 0
153
'''

n = int(input())
gt = 1
tong = 0
for i in range(1, n + 1):
    gt *= i
    tong += gt
print(tong)