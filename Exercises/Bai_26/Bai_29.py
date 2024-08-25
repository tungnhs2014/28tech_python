'''
Cho N số nguyên, nhiệm vụ của bạn là tính tổng các số nguyên được nhập là số chẵn.

Input Format
Dòng đầu tiên là số nguyên dương N - số lượng số được nhập. Dòng thứ 2 là N số nguyên được nhập, mỗi số cách nhau một khoảng trắng

Constraints
1<=N<=100000; Các số được nhập là số nguyên dương không quá 10^6

Output Format
In ra tổng các số chẵn được nhập vào.

Sample Input 0
8
8 9 4 1 5 1 6 6 

Sample Output 0
24
'''

n = int(input())
a = list(map(int, input().split()))
tong = 0
for i in a:
    if i % 2 == 0:
        tong += i
print(tong)