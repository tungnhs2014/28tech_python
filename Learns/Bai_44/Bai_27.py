'''
Nhập vào một số và kiểm tra xem số vừa nhập có phải là số trong dãy fibonacci hay không? Biết rằng số fibonacci bắt đầu bằng 0 và 1.

Input Format
Số nguyên không âm n

Constraints
0≤n≤9*10^18

Output Format
In ra YES nếu n là số Fibonacci, ngược lại in NO

Sample Input 0
0

Sample Output 0
YES

Sample Input 1
18636

Sample Output 1
NO
'''

def check(n):
    if n == 0 or n == 1:
        return True
    fn1 = 1
    fn2 = 0
    for i in range(2, 100):
        fn = fn1 + fn2 
        if fn == n:
            return True
        fn2, fn1 = fn1, fn
    return False

if __name__ == '__main__':
    n = int(input())
    if check(n):
        print('YES')
    else:
        print('NO')