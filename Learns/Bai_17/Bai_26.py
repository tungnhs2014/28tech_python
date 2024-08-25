'''
Cho 4 số nguyên a, b, c, d. Hãy tìm số lớn nhất và nhỏ nhất trong 4 số này.

Input Format

4 số a, b, c, d viết trên 1 dòng và cách nhau một dấu cách.

Constraints

1<=a,b,c,d<=10^18

Output Format

In ra số lớn nhất và nhỏ nhất.

Sample Input 0

546 272 839 508
Sample Output 0

839 272
'''

a, b, c, d = map(int, input().split())
min_val, max_val = a, a

if b > max_val: max_val = b
if c > max_val: max_val = c
if d > max_val: max_val = d

if b < min_val: min_val = b
if c < min_val: min_val = c
if d < min_val: min_val = d

print(max_val, min_val)