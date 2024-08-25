'''
Nhập vào n, tính tổng các chữ số của n, và in ra kết quả

Input Format
Số nguyên không âm n

Constraints
0≤n≤10^18

Output Format
Tổng chữ số của n

Sample Input 0
12341

Sample Output 0
11
'''

n = int(input())
tong = 0
while n != 0:
    tong += n % 10
    n //= 10
print(tong)