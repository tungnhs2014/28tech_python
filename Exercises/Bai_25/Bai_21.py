'''
Nhập n là một số nguyên không quá 100. In ra các hình tương ứng, mỗi hình cách nhau một dòng trống.

Input Format
Số nguyên dương N

Constraints
1≤n≤100

Output Format
In ra hình sao theo mẫu

Sample Input 0
5

Sample Output 0

*****
*****
*****
*****
*****

*****
*   *
*   *
*   *
*****

*****
*###*
*###*
*###*
*****

1 1 1 1 1 
2       2 
3       3 
4       4 
5 5 5 5 5 
'''

n = int(input())

for i in range(0, n):
    for j in range(0, n):
        print('*', end = '')
    print()
print()

for i in range(0, n):
    for j in range(0, n):
        if(i == 0 or i == n-1 or j == 0 or j == n-1):
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
print()

for i in range(0, n):
    for j in range(0, n):
        if(i == 0 or i == n-1 or j == 0 or j == n-1):
            print('*', end = '')
        else:
            print('#', end = '')
    print()
print()


for i in range(1, n+1):
    for j in range(1, n+1):
        if(i == 1 or i == n or j == 1 or j == n):
            print(i, end = ' ')
        else:
            print(' ', end = ' ')
    print()
print()