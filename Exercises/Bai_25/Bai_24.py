'''
Cho 2 số a và b. Nhiệm vụ của bạn là tính ước chung lớn nhất của a giai thừa và b giai thừa

Input Format
2 số nguyên không âm a và b.

Constraints
0<=a,b<=10^12; 0<=min(a, b)<=12

Output Format
In ra kết quả trên 1 dòng

Sample Input 0
2 5
Sample Output 0

2
Explanation 0
2! = 2; 5! = 120. Ước chung lớn nhất của 2 và 120 là 2.
'''

from math import *

a, b = map(int, input().split())
print(factorial(min(a, b)))