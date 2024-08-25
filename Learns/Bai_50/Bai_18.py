'''
Cho số nguyên không âm N, hãy tính tổng các chữ số chẵn, tổng các chữ số lẻ của N.

Input Format
Số nguyên không âm N.

Constraints
0≤n≤10^18

Output Format
Dòng đầu tiên in ra tổng các chữ số chẵn. Dòng thứ 2 in ra tổng các chữ số lẻ.

Sample Input 0
123456

Sample Output 0
12
9
'''

def chan(n):
    if n < 10:
        if n % 2 == 0:
            return n
        else:
            return 0
    else:
        if n % 2 == 0:
            return n % 10 + chan(n // 10)
        else:
            return chan(n // 10)
        
def le(n):
    if n < 10:
        if n % 2 != 0:
            return n
        else:
            return 0
    else:
        if n % 2 != 0:
            return n % 10 + le(n // 10)
        else:
            return le(n // 10)

def in2(n):
    if n < 10:
        print(n, end = ' ')
    else:
        in2(n // 10)
        print(n % 10, end = ' ')

if __name__ == '__main__':
    n = int(input())
    print(chan(n))
    print(le(n))
