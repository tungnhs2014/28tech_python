'''
Một số được gọi là “lộc phát” nếu chỉ có các chữ số 0,6,8.
Nhập vào một số nguyên hãy kiểm tra xem đó có phải số lộc phát hay không. Nếu đúng in ra 1, sai in ra 0.

Input Format
Số nguyên n

Constraints
0≤n≤10^18

Output Format
In ra 1 nếu n là số lộc phát, ngược lại in 0

Sample Input 0

60806
Sample Output 0

1
'''

def check(n):
    while n != 0:
        r = n % 10
        if r != 0 and r != 6 and r != 8:
            return False
        n //= 10
    return True

#code
if __name__ == '__main__':
    n = int(input())
    if check(n):
        print(1)
    else:
        print(0)