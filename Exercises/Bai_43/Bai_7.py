'''
Hãy liệt kê các cặp số nguyên tố cùng nhau và có giá trị khác nhau trong đoạn [a,b] theo thứ tự từ nhỏ đến lớn.

Input Format
Chỉ có một dòng ghi hai số a, b

Constraints
1<=a<=b<=1000

Output Format
Các cặp số i,j thỏa mãn được viết lần lượt trên từng dòng theo định dạng (i,j), theo thứ tự từ điển.

Sample Input 0
5 46
'''

from math import *

if __name__ == '__main__':
    a, b = map(int, input().split())
    for i in range(a, b):
        for j in range(i + 1, b + 1):
            if gcd(i, j) == 1:
                print("(", i, "," ,j, ")", sep = " ")