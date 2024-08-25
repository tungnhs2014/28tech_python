'''
Cho một số nguyên dương n, hãy biểu diễn n dưới dạng tổng của các số nguyên tố sao cho số lượng số hạng trong tổng là lớn nhất có thể.

Input Format
Số nguyên dương N trên 1 dòng

Constraints
1<=N<=10^4

Output Format
Dòng đầu tiên in ra số lượng số hạng trong tổng. Nếu không thể biểu diễn n dưới dạng tổng các số nguyên tố thì in ra -1 cho dòng này 
và không cần in dòng 2. Dòng 2 in ra các số hạng trong tổng theo thứ tự tăng dần.

Sample Input 0
6

Sample Output 0
3
2 2 2 

Sample Input 1
1

Sample Output 1
-1
'''

n = int(input())
if n == 1:
    print(-1)
elif n % 2 == 0:
    print(n // 2)
    for i in range(0, n // 2):
        print(2, end = ' ')
else:
    print(n // 2)
    for i in range(0, n // 2  -1):
        print(2, end = ' ')
    print(3)