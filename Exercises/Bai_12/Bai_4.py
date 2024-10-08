'''
Cho bán kính R của hình tròn. Yêu cầu tính chu vi và diện tích của hình tròn đó. Lấy PI = 3.14. 
Công thức tính chu vi = 2 * PI * R, diện tích = PI * R * R

Input Format
1 dòng chứa bán kính R là số nguyên dương.

Constraints
1≤R≤1000

Output Format
In ra chu vi và diện tích trên 1 dòng, kết quả lấy độ chính xác 4 số sau dấu phẩy.

Sample Input 0
10

Sample Output 0
62.8000 314.0000
'''

PI = 3.14
R = int(input())

CV = 2 * R * PI
DT = PI *R ** 2

print('%.4f' % CV, '%.4f' % DT)

