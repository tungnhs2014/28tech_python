'''
Năm nhuận là năm chia hết cho 400 hoặc (chia hết cho 4 và không chia hết cho 100). 
Nhập vào N là một năm và kiểm tra xem N có phải là năm nhuận hay không?

Input Format
Số nguyên dương N.

Constraints
1<=N<=5000

Output Format
In ra YES nếu N là năm nhuận, ngược lại in ra NO.

Sample Input 0
2020

Sample Output 0
YES
'''

n = int(input())

if (n % 400 == 0) or (n % 4 == 0 and n % 100 != 0):
    print('YES')
else:
    print('NO')
