'''
Một số được coi là số đẹp nếu nó là số thuận nghịch, có chứa ít nhất một chữ số 6, và tổng các chữ số của nó có chữ số cuối cùng là 8. 
Viết chương trình liệt kê các số đẹp trong đoạn giữa 2 số nguyên cho trước, các số cách nhau một dấu cách.

Input Format
2 số nguyên a, b

Constraints
1≤a≤b≤10^6

Output Format
Liệt kê các số đẹp trong đoạn, các số viết cách nhau một khoảng trống

Sample Input 0

1 400

Sample Output 0
161

'''

def check(n):
    temp = n
    rev = 0
    tong = 0
    ok = False
    while n != 0:
        rev = rev * 10 + n % 10
        if n % 10 == 6:
            ok = True
        tong += n % 10
        n //= 10
    return ok and (temp == rev) and (tong % 10 == 8)

#code
if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b + 1):
        if check(i):
            print(i, end = ' ')