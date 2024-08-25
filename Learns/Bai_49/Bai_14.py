'''
Cho một số nguyên không âm N, hãy đếm số lượng chữ số của N.

Input Format
Số nguyên không âm N

Constraints
0≤n≤10^18

Output Format
Số lượng chữ số của N.

Sample Input 0
123452

Sample Output 0
6
'''

def S(n):
    if n < 10:
        return 1
    else:
        return 1 + S(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(S(n))