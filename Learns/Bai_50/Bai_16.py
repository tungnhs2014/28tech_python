'''
Cho một số nguyên không âm N, hãy in ra chữ số lớn nhất và chữ số nhỏ nhất của N. Viết 2 hàm đệ quy

Input Format
Số nguyên dương N

Constraints
10≤n≤10^18

Output Format
Chữ số lớn nhất và nhỏ nhất của N.

Sample Input 0
1256782

Sample Output 0
8 1
'''

def S1(n):
    if n < 10:
        return n
    else:
        return max(n % 10, S1(n // 10))

def S2(n):
    if n < 10:
        return n
    else:
        return min(n % 10, S2(n // 10))


if __name__ == '__main__':
    n = int(input())
    print(S1(n), S2(n))