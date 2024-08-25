'''
Cho số nguyên n không âm. Viết hàm xử lý các yêu cầu sau
Kiểm tra n là số nguyên tố, nếu đúng in 1, sai in 0.

In tổng chữ số của n.

In tổng chữ số chẵn của n.

In tổng chữ số của n là số nguyên tố.

In số lật ngược của n. Ví dụ 123 in 321.

In số lượng ước của n là số nguyên tố (làm tương tự như phân tích thừa số ng tố).

In ước nguyên tố lớn nhất của n (làm tương tự như phân tích thừa số ng tố).

Kiểm tra nếu n tồn tại ít nhất 1 số 6, nếu đúng in 1, sai in 0.

Kiểm tra nếu tổng chữ số của n chia hết cho 8, nếu đúng in 1, sai in 0.

Tính tổng giai thừa các chữ số của n và in ra. Ví dụ n = 123, tổng = 1! + 2! +3
!
Kiểm tra n có phải chỉ được tạo bởi 1 số hay không? Ví dụ 222, 333, 99999. Đúng in ra 1, sai in ra 0.

Kiểm tra n có phải có chữ số tận cùng là lớn nhất hay không, tức là không có chữ số nào của n lớn hơn chữ số hàng đơn vị của nó. nếu đúng in 1, sai in 0.
In tổng lũy thừa chữ số của n với số mũ là số chữ số. ví dụ 123 thì tính 1^3+2^3+3^3.

Input Format
Số duy nhất n

Constraints
2<=n<=1000;

Output Format
In ra 13 dòng tương ứng với các yêu cầu ở trên.

Sample Input 0
36

Sample Output 0
0
9
6
3
63
2
3
1
0
726
0
1
45
'''

from math import *

#Hàm 1
def Ham_1(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return 0
    return 1

#Hàm 2
def Ham_2(n):
    tong = 0
    while n !=0:
        tong += n % 10
        n //= 10
    return tong

#Hàm 3
def Ham_3(n):
    tong = 0
    while n !=0:
        if n % 10 % 2 == 0:
            tong += n % 10
        n //= 10
    return tong

#Hàm 4
def Ham_4(n):
    tong = 0
    while n !=0:
        r = n % 10
        if r == 2 or r == 3 or r == 5 or r == 7:
            tong += r
        n //= 10
    return tong

#Hàm 5
def Ham_5(n):
    tmp = 0
    while n !=0:
        tmp = tmp * 10 + n % 10
        n //= 10
    return tmp

#Hàm 6
def Ham_6(n):
    dem = 0
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            dem +=1
            while(n % i == 0):
                n //= i
    if n > 1:
        dem += i
    return dem

#Hàm 7
def Ham_7(n):
    res = -1
    for i in range(2,isqrt(n) + 1):
        if n % i == 0:
            res = i
            while(n % i == 0):
                n //= i
    if n > 1:
        res = n
    return res

#Hàm 8
def Ham_8(n):
    while n != 0:
        if n % 10 == 6:
            return 1
        n //= 10
    return 0

#Hàm 9
def Ham_9(n):
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    if tong % 8 == 0:
        return 1
    else:
        return 0
    
#Hàm 10
def Ham_10(n):
    tong = 0
    while n != 0:
        tong += factorial(n % 10)
        n //= 10
    return tong

#Hàm 11
def Ham_11(n):
    donvi = n % 10
    while n != 0:
        if(n % 10 != donvi):
            return 0
        n //= 10
    return 1
        
#Hàm 12
def Ham_12(n):
    donvi = n % 10
    while n != 0:
        if n % 10 > donvi:
            return 0
        n //= 10
    return 1

#Hàm 13
def Ham_13(n):
    m = n
    cnt = 0
    while n != 0:
        cnt += 1
        n //= 10
    tong = 0
    while m != 0:
        tong += (m % 10) ** cnt
        m //= 10
    return tong

if __name__ == '__main__':
    n = int(input())
    print(Ham_1(n))
    print(Ham_2(n))
    print(Ham_3(n))
    print(Ham_4(n))
    print(Ham_5(n))
    print(Ham_6(n))
    print(Ham_7(n))
    print(Ham_8(n))
    print(Ham_9(n))
    print(Ham_10(n))
    print(Ham_11(n))
    print(Ham_12(n))
    print(Ham_13(n))


