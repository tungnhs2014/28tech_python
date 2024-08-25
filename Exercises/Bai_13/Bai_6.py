'''
Cho một số nguyên không âm N.Bạn hãy thực hiện viết câu lệnh để kiểm tra các điều kiện sau :

1. N có phải là số chẵn? (Kiểm tra số dư của N với 2 và so sánh 0)

2. N có phải là số vừa chia hết cho 3 vừa chia hết cho 5? (Kết hợp 2 điều kiện sử dụng &&)

3. N có phải là số chia hết 3 nhưng không chia hết cho 7? (Kết hợp 2 điều kiện sử dụng &&)

4. N có phải là số chia hết cho 3 hoặc 7? (Kết hợp 2 điều kiện sử dụng ||)

5. N là số lớn hơn 30 và nhỏ hơn 50? (Kết hợp 2 điều kiện sử dụng &&)

6. N có phải là số không nhỏ hơn 30 và chia hết cho ít nhất một trong 3 số 2, 3, 5? (Lớn hơn hoặc bằng 30 && (chia hết ....

7. N có phải là số có 2 chữ số có chữ tận cùng là một số nguyên tố? (>= 10, <= 99, kiểm tra chữ số tận cùng là 2, 3, 5, 7)

8. N có phải là số không vượt quá 100 và chia hết cho 23?

9. N không thuộc đoạn [10, 20]?

10. N có chữ số tận cùng là bội số của 3?

Input Format
Số nguyên dương N

Constraints
1<=N<=10^6

Output Format
In ra 10 dòng, mỗi dòng là "YES" hoặc "NO" tương ứng với 10 điều kiện. Nếu N thỏa mãn điều kiện thứ i thì dòng i in ra YES, ngược lại in ra NO.

Sample Input 0

263
Sample Output 0

NO
NO
NO
NO
NO
NO
NO
NO
YES
YES
Sample Input 1

380
Sample Output 1

YES
NO
NO
NO
NO
YES
NO
NO
YES
YES
Sample Input 2

52
Sample Output 2

YES
NO
NO
NO
NO
YES
YES
NO
YES
NO
'''

n = int(input())
#1
if n % 2 == 0:
    print('YES')
else:
    print('NO')

#2
if n % 3 == 0 and n % 5 == 0:
    print('YES')
else:
    print('NO')

#3
if n % 3 == 0 and n % 7 != 0:
    print('YES')
else:
    print('NO')  

#4
if n % 3 == 0 or n % 7 == 0:
    print('YES')
else:
    print('NO') 

#5
if (n > 30 and n <50) == True:
    print('YES')
else:
    print('NO') 

#6
if ((n >= 30) and (n % 2 == 0 or n % 3 ==0 or n % 5 == 0)):
    print('YES')
else:
    print('NO') 

#7
r = n % 10
if (n >= 10 and n <=99) or (r == 2 or r == 3 or r == 5 or r ==7):
    print('YES')
else:
    print('NO')

#8
if (n <= 100) and (n % 23 == 0):
    print('YES')
else:
    print('NO')

#9
if n < 30 or n > 20:
    print('YES')
else:
    print('NO')

#10
if r % 3 == 0:
    print('YES')
else:
    print('NO')