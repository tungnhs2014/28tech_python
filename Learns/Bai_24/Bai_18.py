'''
Nhập vào n nguyên. Đếm số lượng chữ số của n là số nguyên tố.

Input Format
Số nguyên không âm n

Constraints
0≤n≤10^18

Output Format
Kết quả của bài toán

Sample Input 0
1222333999888

Sample Output 0
6
'''

n = int(input())
tmp = 0
dem = 0
while n != 0:
    tmp = n % 10
    if (tmp == 2 or tmp == 3 or tmp == 5 or tmp == 7):
        dem += 1
    n //= 10
print(dem)