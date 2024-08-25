'''
Nhập vào n nguyên dương không quá 10^6, tính và in tổng sau ra màn hình S=2+4+6+8+.....+2*n

Input Format
Số nguyên dương n

Constraints
1≤n≤10^6

Output Format
Kết quả của bài toán

Sample Input 0
4
Sample Output 0
20

'''

n = int(input())
tong = 0
for i in range(1, n + 1):
    tong += 2*i
print(tong)