'''
In ra các số chính phương trong đoạn từ a tới b. Bài này bạn nào code bằng java thì có thể bỏ qua vì test lớn quá Java không chạy xong trong 8s.

Input Format
2 số nguyên dương a, b

Constraints
1≤a≤b≤10^12

Output Format
In ra các số chính phương trong đoạn giữa 2 số a, b trên một dòng. Các số cách nhau một khoảng trắng.

Sample Input 0
10 20

Sample Output 0
16
'''
from math import *

if __name__ == '__main__':
    a, b = map(int, input().split())
    can1, can2 = isqrt(a), isqrt(b)
    if can1 ** 2 != a:
        can1 += 1
    for i in range(can1, can2 + 1):
        print(i * i, end = ' ')
