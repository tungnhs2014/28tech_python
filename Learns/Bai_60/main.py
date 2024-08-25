from math import *

#Dạng 4: Mảng đánh dấu: Sử dụng chỉ số của mảng để đánh dấu  1 giá trị tương ứng
# + Giá trị khác nhau trong mảng: Tìm số lượng phần tử khác nhau, liệt kê
# + Những bài toán liên quan đến tần suất

# Cho mảng A[] gồm N phần tử, đếm xem mỗi phần tử trong mảng xuất hiện bao nhiêu lần

# Chỉ áp dụng với những phần tử >= 0 và <= 10^7

'''
Input:
8
1 2 1 2 3 1 4 2

Output:
1 3
2 3
3 1
4 1
'''
'''
# liệt kê, đếm các phần tử thỏa mãn tính chất nào đó trong list
if __name__ == '__main__':
    a = [4, 1, 2, 1, 2, 3, 1, 4 ,2]
    cnt = [0] * 10000001
    #0 => 10^7
    for x in a:
        cnt[x] += 1
    # l, r = min(a), max(a)
    # for i in range(l, r + 1):
    #     print(i, cnt[i])
        
    for x in a:
        if cnt[x] != 0:
            print(x, cnt[x])
            cnt[x] = 0
'''
'''
if __name__ == '__main__':
    a = [4, 1, 2, 1, 2, 3, 1, 4 ,2]
    cnt = [0] * 10000001
    for x in a:
        cnt[x] = 1 # x đã xuất hiện
    l, r = min(a), max(a)
    dem = 0        
    for i in range(l, r + 1):
        if cnt[i] != 0:
            dem += 1
            print(i, end = ' ')
    print()
    print(dem)
'''

if __name__ == '__main__':
    a = [4, 1, 2, 1, 2, 3, 1, 4, 2, 5]
    cnt = [0] * 10000001
    for x in a:
        cnt[x] = 1 # x đã xuất hiện
    for x in a:
        if cnt[x] != 0:
            print(x, end = ' ')
            cnt[x] = 0
