'''
Cho 2 số nguyên không âm a và b. Hãy tính a^b%(10^9+7). Kiến thức bạn cần sử dụng là Binary Exponentiation.

Input Format
2 số nguyên dương a, b

Constraints
1≤a,b≤10^9

Output Format
In ra kết quả của bài toán.

Sample Input 0
2 10

Sample Output 0
1024
'''

def binpow(a, b):
    if b == 0:
        return 1
    #di tinh a ^b // 2
    X = binpow(a, b // 2)
    if b % 2 == 1:
        return X * X * a % (10 ** 9 + 7)
    else:
        return X * X % (10 ** 9 + 7)
    
if __name__ == '__main__':
    a, b= map(int, input().split())
    print(binpow(a, b))
