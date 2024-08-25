'''
Cho số nguyên không âm N, hãy kiểm tra xem tất cả các chữ số của N có phải đều là số chẵn hay không?

Input Format
Số nguyên không âm N.

Constraints
0≤n≤10^18

Output Format
In ra YES nếu n toàn chữ số chẵn, ngược lại in ra NO.

Sample Input 0
2280820

Sample Output 0
YES
'''

def check(n):
    if n < 10:
        if n % 2 == 0:
            return True
        else:
            return False
    else:
        if n % 2 == 1:
            return False
        else:
            return check(n // 10)
        
if __name__ == '__main__':
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')