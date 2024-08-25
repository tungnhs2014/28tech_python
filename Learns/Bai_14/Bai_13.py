'''
Cho trước N ngày, hãy đổi N thành số năm, số tuần và số ngày. Biết rằng một năm có 365 ngày.

Input Format
Số nguyên không âm N

Constraints
0<=N<=1000000

Output Format
In ra số năm, tuần, ngày tương ứng với N ngày

Sample Input 0
373

Sample Output 0
1 1 1
'''

n = int(input())
nam = n // 365
n = n % 365
tuan = n // 7
n = n % 7
print(nam, tuan , n)