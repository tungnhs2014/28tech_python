'''
Cho một kí tự, bạn hãy kiểm tra kí tự nhập vào là chữ cái in hoa, in thường, chữ số hay kí tự đặc biệt(các kí tự không phải là chữ cái và chữ số)

Input Format
1 dòng chứa kí tự c

Constraints
c là chữ in hoa, in thường, chữ số hoặc kí tự đặc biệt

Output Format
Nếu c là chữ cái in hoa in ra "UPPER". Nếu c là chữ cái in thường in ra "LOWER". Nếu c là chữ số in ra "DIGIT". Nếu c là kí tự đặc biệt in ra "SPECIAL".

Sample Input 0
Z
Sample Output 0

UPPER
'''

#A-Z: 65-> 90
#a-z: 97-> 122
#0-9: 48-> 57

c = input()
if c.islower():
    print('LOWER')
elif c.isupper():
    print('UPPER')
elif c.isdigit():
    print('DIGIT')
else:
    print('SPECIAL')