'''
Nhiệm vụ của bạn là in ra N số Fibonacci đầu tiên, một số đầu tiên trong dãy Fibonacci là 1, 1, 2, 3, 5, 8....

Input Format
Dòng duy nhất chứa số nguyên dương N

Constraints
1<=N<=92

Output Format
In ra N số Fibonacci đầu tiên, mỗi số trên 1 dòng

Sample Input 0
6

Sample Output 0
1
1
2
3
5
8
'''
if __name__ == '__main__':
    n = int(input())
    if n == 1:
        print(1)
    elif n == 2:
        print('1 \n1')
    else:
        print('1 \n1')
        fn1 = 1
        fn2 = 1
        for i in range(3, n + 1):
            fn = fn1 + fn2
            print(fn)
            fn2, fn1 = fn1 , fn