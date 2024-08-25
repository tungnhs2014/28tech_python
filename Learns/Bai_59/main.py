from math import *

#Dạng 1: Kiểm tra các phần tử trong list thỏa mãn tính chất nào đó
#Dạng 2: Tìm max, min: O(n)
#Dạng 3: Kiểm tra các cặp phần tử trong list thỏa mãn điều kiện gì đó O(n ^ 2)
#Dạng 4: Mảng đánh dấu

def nt(n):
    if n < 2:
        return False
    for i in range(2, isqrt(n) + 1):
        if n % i == 0:
            return False
    return True

# liệt kê, đếm các phần tử thỏa mãn tính chất nào đó trong list
if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    for x in a:
        if nt(x):
            print(x, end = ' ')
    print()

    min_val, max_val = 10 ** 18, -10 ** 18
    for x in a:
        if x < min_val:
            min_val = x
        if x > max_val:
            max_val = x
    print(min_val, max_val)

    dem = 0
    for i in range(n):
        #đối với mỗi chỉ số i => duyệt các chỉ số từ i + 1 tới n - 1
        for j in range(i + 1, n):
            if gcd(a[i], a[j]) == 1:
                dem += 1
    print(dem)
