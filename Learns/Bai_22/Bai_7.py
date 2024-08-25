'''
Đếm số lượng ước và liệt kê các ước theo thứ tự tăng dần của số nguyên dương N

Input Format
Số nguyên dương N không quá

Constraints
1≤N≤10^6

Output Format
Kết quả của bài toán

Sample Input 0
28

Sample Output 0
6
1 2 4 7 14 28
'''

n = int(input())
dem = 0
for i in range(1, n + 1):
    if n % i == 0:
        dem += 1
print(dem)        
for i in range(1, n + 1):
    if n % i == 0:
         print(i, end = ' ')