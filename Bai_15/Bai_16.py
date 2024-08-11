'''
Cho kí tự là chữ cái in hoa hoặc in thường, in ra kí tự kế tiếp sau nó trong bảng chữ cái ở dạng in thường, 
tức là kí tự nhập vào ở dạng in hoa hay in thường thì bạn đều in ra kí tự kế tiếp nó nhưng ở dạng in thường. Coi kí tự kế tiếp của của chữ Z là chữ A.

Input Format
1 dòng chứa kí tự c

Constraints
c là chữ cái in hoa hoặc in thường

Output Format
In ra chữ cái kế tiếp ở dạng in thường

Sample Input 0
A

Sample Output 0
b

Sample Input 1
z

Sample Output 1
a
'''

n = input()

if n == 'z' or n == 'Z':
    print('a')
else:
    tmp = ord(n) #ord: chuyen doi 1 ky tu thanh ma ASCII
    tmp += 1
    print(chr(tmp).lower()) #chr: chuyen doi ma ASCII thanh ky tu