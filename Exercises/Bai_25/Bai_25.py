'''
Cho số nguyên dương N, bạn hãy tính tổng : S(N) = 1/0! + 1/1! + 1/2! + 1/3! +... + 1/(N - 1)!. Trong đó ! là kí hiệu của giai thừa

Input Format
Dòng duy nhất chứa số nguyên dương N

Constraints
2<=N<=15

Output Format
In ra kết quả lấy độ chính xác 4 số đằng sau dấu thập phân

Sample Input 0
4

Sample Output 0
2.6667
'''

import math

n = int(input())
res = 0
for i in range(n):
    res += 1 / math.factorial(i)
print('%.4f' %res)