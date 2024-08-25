'''
Nhập vào n, đếm số lượng chữ số của n và in ra kết quả.

Input Format
Số nguyên không âm n

Constraints
0≤n≤10^18

Output Format
Số lượng chữ số của n

Sample Input 0
123456789

Sample Output 0
9
'''

n = int(input())

dem = 0

if n == 0:
    print(1)
else:
    while n > 0:
        dem +=1
        n //= 10
    print(dem)