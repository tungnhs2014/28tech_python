'''
Nhập n không âm không quá 15, tính và in ra n!

Input Format
Số nguyên không âm n

Constraints
1≤n≤15

Output Format
Kết quả của bài toán

Sample Input 0
5

Sample Output 0
120
'''

n = int(input())
tong = 1
for i in range(1, n + 1):
    tong *=i
print(tong)