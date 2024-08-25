'''
Tính tổng : S= -1 + 2 - 3 + 4 - 5 + ...... + (-1)^n*n

Input Format
Số nguyên dương n

Constraints
1≤n≤10^6

Output Format
Kết quả của bài toán

Sample Input 0
6

Sample Output 0
3
'''

n = int(input())
s = 0
for i in range(1, n + 1):
    if i % 2 == 0:
        s += i
    else:
        s -= i
print(s)