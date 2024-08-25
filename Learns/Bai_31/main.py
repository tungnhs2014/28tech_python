import math

#Số chính phương
def Square(n):
    can = math.isqrt(n)
    if can * can == n:
        return True
    else:
        return False
    
#Số lập phương
def Cube(n):
    can = int(math.pow(n, 1/3))
    return can ** 3 == n or ((can + 1) ** 3 == n)

if __name__ == '__main__':
    n = int(input())
    if Cube(n):
        print('YES')
    else:
        print('NO')