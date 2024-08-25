'''
Kiểm tra một số có phải là số Fibonacci hay không, bạn phải trả lời nhiều trường hợp trong bài toán này.

Input Format
Dòng đầu tiên là số lượng bộ test T; T dòng tiếp theo mỗi dòng là một số nguyên dương N;

Constraints
1<=T<=100; 1<=N<=10^18

Output Format
Đối với mỗi test case in kết quả trên một dòng, nếu là số Fibonacci in YES, ngược lại in NO.

Sample Input 0
5
89
754
399
34
661

Sample Output 0
YES
NO
NO
YES
NO
'''

from math import *

def check_fibo(n):
    if n == 1:
        return True
    fn1, fn2 = 1, 1
    for i in range(2, 100):
        fn = fn1 + fn2
        if fn == n:
            return True
        fn2, fn1 = fn1, fn
    return False


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        if check_fibo(n):
            print('YES')
        else:
            print('NO')
