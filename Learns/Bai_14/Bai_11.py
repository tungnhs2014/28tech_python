'''
Cho 3 cạnh a, b, c của một tam giác, nếu tam giác đã cho là tam giác đều thì in ra 1, 
tam giác cân thì in ra 2, tam giác vuông thì in ra 3, tam giác thường in ra 4, 
trường hợp tam giác nhập vào không hợp lệ thì in ra "INVALID".

Input Format
1 dòng chứa 3 số a, b, c.

Constraints
0<=a,b,c<=10^3

Output Format
In ra kết quả tương ứng.

Sample Input 0
8 8 8 

Sample Output 0
1

Sample Input 1
8 8 6

Sample Output 1
2
'''

a, b, c = map(int, input().split())

if a > 0 and b > 0 and c > 0 and a + b > c and a + c > b and b + c > a:
    if a == b and a == c and b == c:
        print(1)
    elif a == b or a == c or b == c:
        print(2)
    elif (a*a == b *b + c*c) or (b*b == a*a + c*c) or (c*c == a*a + b*b):
        print(3)
    else:
        print(4)

else:
    print('INVALID')
