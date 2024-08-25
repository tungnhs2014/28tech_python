'''
Nhập vào n nguyên dương không quá 1000 và tính tổng sau, kết quả in ra màn hình. S=1^3+2^3+3^3+4^3+……+n^3.

Input Format
Số nguyên dương n

Constraints
1≤n≤10^3

Output Format
Kết quả của bài toán

Sample Input 0
3

Sample Output 0
36
'''

n = int(input())
s = 0
for i in range(1, n + 1):
    s += i ** 3
print(s)