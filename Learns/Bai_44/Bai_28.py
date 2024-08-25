'''
Nhiệm vụ của bạn là hãy tìm số thuộc dãy số Fibonacci nhỏ nhất lớn hơn hoặc bằng số N đã cho. 
Biết một số đầu tiên trong dãy Fibonacci là : 1, 1, 2, 3, 5, 8, 13....

Input Format
Dòng duy nhất chứa số nguyên dương N

Constraints
1<=N<=10^18

Output Format
In ra số Fibonacci nhỏ nhất lớn hơn hoặc bằng N

Sample Input 0
12

Sample Output 0
13
'''


def check(n):
    if n == 0 or n == 1:
        return True
    fn1 = 1
    fn2 = 0
    for i in range(2, 100):
        fn = fn1 + fn2 
        if fn >= n:
            return fn
        fn2, fn1 = fn1, fn
    return -1

if __name__ == '__main__':
    n = int(input())
    print(check(n))