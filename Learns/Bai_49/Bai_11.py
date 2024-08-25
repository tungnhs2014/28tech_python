'''
Cho một số nguyên không âm N, hãy in ra dạng biểu diễn nhị phân của số N.

Input Format
Số nguyên không âm N

Constraints
0≤n≤10^18

Output Format
Biểu diễn nhị phân của số nguyên N.

Sample Input 0
8

Sample Output 0
1000
'''

def nhiphan(n):
    if n != 0:
        nhiphan(n // 2)
        print(n % 2, end = '')


if __name__ == '__main__':
    n = int(input())
    if n == 0: print(0)
    else:
        nhiphan(n)