'''
Cho một số thực a, hãy tìm số nguyên gần a nhất. Trong trường hợp phần thực của a = 0.5 thì làm tròn lên

Input Format
Số thực a

Constraints
0<=a<=10^6

Output Format
Số nguyên gần với a nhất

Sample Input 0

15.2
Sample Output 0
15
'''
import math

a = float(input())

if a - int(a) >= 0.5:
    print(math.ceil(a))
else:
    print(math.floor(a))