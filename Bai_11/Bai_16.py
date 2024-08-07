'''
Bài tập này rất đơn giản, bạn được yêu cầu nhập vào 4 số x, y, z, t và in ra theo mẫu. 
Dòng 1 : In ra x, y, z, t mỗi số cách nhau 2 khoảng trắng. 
Dòng 2 in ra y, z, x, t mỗi số cách nhau 2 dấu gạch giữa. 
Dòng 3 in ra 2 * x, 3 * y, 4 * z, 5 * t cách nhau 1 dấu phẩy. 
Dòng 4 in ra "KET THUC !!". 
Giữa các dòng có 1 dòng trống

Chú ý in ra đúng thứ tự đề bài yêu cầu.

Input Format
1 dòng duy nhất chứa 4 số nguyên x, y, z, t viết cách nhau 10 dấu cách 
(Thực ra thì cin nó bỏ qua tất cả mọi dấu cách nên 10 hay 1 dấu cách thì bạn vẫn nhập như bình thường)

Constraints
1<=x,y,z,t<=10^9;

Output Format
In ra két quả cùa bài toán

Sample Input 0
8          9          2          10

Sample Output 0
8  9  2  10

9--2--8--10

16,27,8,50

KET THUC !!

Sample Input 1
2          2          9          9

Sample Output 1
2  2  9  9

2--9--2--9

4,6,36,45

KET THUC !!
'''

x, y, z, t = map(int, input().split())

print(x, y, z, t, sep = '  ', end = '\n\n')
print(y, z, x, t, sep = '--', end = '\n\n')
print(2*x, 3*y, 4*z, 5*t, sep = ',', end = '\n\n')
print('KET THUC !!')


