'''
Cho một số nguyên không âm N, hãy in ra chữ số đầu tiên của N.

Input Format
Số nguyên không âm N

Constraints
0≤n≤10^18

Output Format
In ra chữ số đầu tiên của N.

Sample Input 0
56721

Sample Output 0
5
'''

def S(n):
    if n < 10:
        return n
    else:
        return S(n // 10)


if __name__ == '__main__':
    n = int(input())
    print(S(n))