'''
Cho một số nguyên không âm N, hãy in ra dạng biểu diễn của N dưới hệ 16.

Input Format
Số nguyên không âm N

Constraints
0≤n≤10^18

Output Format
Biểu diễn hệ 16 của số nguyên N.

Sample Input 0
995

Sample Output 0
3E3
'''

def F(n):
    if n != 0:
        F(n // 16)
        r = n % 16
        if r < 10:
            print(r, end = '')
        else:
            print(chr(r + 55), end = '') # A: 65 => 65- 10 = 55


if __name__ == '__main__':
    n = int(input())
    if n == 0: print(0)
    else:
        F(n)