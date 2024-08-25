#Số fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...
#Số fibonacci: Kiểm tra 1 số có phải là số fibo, in ra số fibonacci thứ n, hoặc in ra n số fibonacci đầu tiên

import math

#C/C++/Java: 0<=N<=10^18
#0 => n -1

def fibo(n):
    if n == 0:
        print(0)
    elif n == 1:
        print('0 1')
    else:
        print('0 1', end = '\n')
        fn1, fn2 = 1, 0
        for i in range(2, n):
            fn = fn1 + fn2
            print(fn, end = '\n')
            fn2, fn1 = fn1, fn

def checkfibo(n):
    if n == 0 or n == 1:
        return True
    fn1, fn2 = 1, 0
    for i in range(2, 93):
        fn = fn1 + fn2
        if fn == n:
            return True
        fn2, fn1 = fn1, fn
    return False

def printFibo(n):
    if n == 0 or n == 1:
        return n
    fn1, fn2 = 1, 0
    for i in range(2, n + 1):
        fn = fn1 + fn2
        fn2, fn1 = fn1, fn
    return fn

if __name__ == '__main__':
    fibo(100)
    print(checkfibo(24))
    print(printFibo(143))
