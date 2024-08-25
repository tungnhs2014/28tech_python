
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
*
**
***
****
*****

*****
****
***
**
*

    *
   **
  ***
 ****
*****

*****
 ****
  ***
   **
    *

*
**
* *
*  *
*****
'''

n = int(input())

for i in range(1, n + 1):
    #dong i: lop i lan
    for j in range(i):
        print('*', end = '')
    print()
print()

for i in range(n, 0, -1):
    #dong i: lop i lan
    for j in range(i):
        print('*', end = '')
    print()
print()

for i in range(1, n + 1):
    #dong i: j <= n - i: cach, *
    for j in range(1, n + 1):
        if j <= n - i:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()
print()

for i in range(1, n + 1):
    #dong i: j <= n - i: cach, *
    for j in range(1, n + 1):
        if j < i:
            print(' ', end = '')
        else:
            print('*', end = '')
    print()
print()

for i in range(1, n + 1):
    #dong i: lop i lan
    for j in range(1, i + 1):
        if i == 1 or i == n or j == 1 or j == i:
            print('*', end = '')
        else:
            print(' ', end = '')
    print()
print()