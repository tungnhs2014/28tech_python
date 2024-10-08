'''
Bài này các bạn sử dụng cả 2 vòng lặp for và while để code. Lượt 1 sử dụng for, lượt 2 dùng while. 
Cho số tự nhiên N, nhiệm vụ của bạn in ra các dãy số bằng vòng lặp trên từng dòng, mỗi số cách nhau một dấu cách.

Dòng 1. In ra các số từ 1 tới n.
Dòng 2 in ra các số từ n về 0.
Dòng 3 in ra các số chẵn nhỏ hơn hoặc bằng n.
Dòng 4 in ra các số lẻ nhỏ hơn hoặc bằng n.
Dòng 5 in ra các bội số của 4 nhỏ hơn n.
Dòng 6 in ra N chữ cái in thường đầu tiên.
Dòng 7 in ra N chữ cái in thường cuối cùng theo thứ tự tăng dần.

Input Format
Dòng duy nhất chứa số nguyên dương N

Constraints
5<=N<=26

Output Format
In ra 7 dòng theo yêu cầu

Sample Input 0
5

Sample Output 0
1 2 3 4 5 
5 4 3 2 1 0 
0 2 4 
1 3 5 
0 4 
a b c d e 
v w x y z 
'''

n = int(input())
#1
for i in range(1, n + 1):
    print(i, end = ' ')
print()
#2
temp = n
while (temp >=0):
    print(temp, end = ' ')
    temp -= 1

print()
#3
for i in range(0, n + 1, 2):
    print(i, end = ' ')
print()
temp = 0
#4
while(temp <= n):
    if (temp % 2 != 0):
        print(temp, end = ' ')
    temp += 1
print()
#5
for i in range(0, n + 1, 4):
    print(i, end = ' ')
print()
#6
for i in range(0, n + 1):
    print(chr(97 + i), end = ' ')
print()
#7
for i in range(122 -n + 1, 123):
    print(chr(i), end = ' ')
print()