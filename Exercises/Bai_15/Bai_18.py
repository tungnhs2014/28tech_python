"""
Cho kí tự c, nếu kí tự c là chữ cái in thường thì chuyển nó thành chữ cái in hoa tương ứng và ngược lại nếu c là chữ cái in hoa thì chuyển nó thành chữ cái in thường tương ứng. 
Trường hợp kí tự nhập vào không phải là chữ cái thì không thay đổi nó.

Input Format
1 dòng chứa kí tự c

Constraints
c có thể là chữ in hoa, in thường, chữ số hoặc kí tự đặc biệt.

Output Format
In ra kết quả theo yêu cầu

Sample Input 0
e
Sample Output 0
E
Sample Input 1

$
Sample Out
"""

c = input()

if c.islower():
    print(c.upper())
elif c.isupper():
    print(c.lower())
else:
    print(c)