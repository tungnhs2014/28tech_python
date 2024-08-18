'''
Đếm số lượng các số chính phương trong đoạn từ a tới b

Input Format
2 số nguyên dương a, b

Constraints
1≤a≤b≤10^18

Output Format
Số lượng số chính phương trong đoạn [a, b]

Sample Input 0
1 1000000000

Sample Output 0
31622
'''


import math

#code
if __name__ == '__main__':
    a, b = map(int, input().split())
    can1, can2 = math.isqrt(a), math.isqrt(b)
    if can1 * can1 != a:
        can1 += 1
    if(can2 + 1) * (can2 + 1) == b:
        can2 += 1
    print(can2 - can1 + 1)