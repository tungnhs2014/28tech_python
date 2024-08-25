'''
Liệt kê các số chính phương dương và không vượt quá n

Ví dụ N = 20 => 1, 4, 9, 16
Gợi ý : Duyệt các số tự nhiên i <= căn N, khi đó i * i sẽ là số chính phương và sẽ <= N

Input Format
Số nguyên dương n

Constraints
1≤n≤10^10.

Output Format
Liệt kê các số chính phương không vượt quá n

Sample Input 0
50

Sample Output 0
1 4 9 16 25 36 49
'''

from math import *

n = int(input())

for i in range(1, isqrt(n) + 1):
    if(i * i <= n):
        print(i * i, end = ' ')