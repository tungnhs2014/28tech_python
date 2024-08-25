'''
Tính tích các ước của số tự nhiên N

Input Format
Số nguyên dương N

Constraints
1≤N≤1000

Output Format
Tích các ước số của N

Sample Input 0
10

Sample Output 0
100
'''

n = int(input())
tich = 1
for i in range(1, n + 1):
    if(n % i == 0):
        tich *= i
print(tich)