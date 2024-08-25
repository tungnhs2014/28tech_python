'''
Cho biết tháng và năm, hãy in ra số ngày tương ứng có trong tháng đó. 
Chú ý tháng 2 của năm nhuận có 29 ngày. Năm nhuận là năm chia hết cho 400 hoặc (chia hết cho 4 và không chia hết cho 100)

Input Format
2 số nguyên t và n tương ứng với tháng và năm.

Constraints
0<=t<=100; 0<=n<=5000;

Output Format
Nếu tháng là hợp lệ(tháng 1 tới 12) và năm là hợp lệ (lớn hơn 0) thì in ra số ngày tương ứng của năm đó, ngược lại in ra "INVALID".

Sample Input 0
11 2021

Sample Output 0
30
'''

t, n = map(int, input().split())

if t >= 1 and t <= 12 and n > 0:
    if t == 1 or t == 3 or t == 5 or t == 7 or t == 8 or t == 10 or t == 12:
        print(31)
    elif t == 4 or t == 6 or t == 9 or t == 11:
        print(30)
    else:
        if n % 400 == 0 or (n % 4 == 0 and n % 100 != 0):
            print(29)
        else:
            print(28)
else:
    print('INVALID')