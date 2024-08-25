'''
Cho 3 số a, b, n. Nhiệm vụ của bạn là xác định xem phương trình ax + by = n có tồn tại cặp nghiệm (x, y) nguyên không âm hay không?

Input Format
1 dòng duy nhất chứa 3 số a, b, n

Constraints
1<=a,b,n<=1000

Output Format
In ra YES nếu tồn tại cặp nghiệm nguyên không âm, ngược lại in ra NO.

Sample Input 0
7 10 16

Sample Output 0
NO

Sample Input 1
5 8 28

Sample Output 1
YES
'''

a, b, n = map(int, input().split())

for i in range(1, n // a + 1):
    check = False
    temp = n - a*i
    if temp % b == 0:
        check = True
        break
if \
    check: print('YES')
else: print('NO')