'''
Nhập vào giá trị của n không quá 10^6, tính tổng các số nguyên dương không vượt quá n, chia hết cho 3.

Gợi ý : Tạo 1 biến kết quả gọi là tong và khởi tạo bằng 0(tránh giá trị rác), sau đó sinh ra 1 vòng lặp chạy từ 1 tới n, 
mỗi vòng lặp thì kiểm tra xem i chia hết cho 3 thì cộng biến i của vòng lặp vào biến tổng. In ra biến tong SAU KHI VÒNG LẶP KẾT THÚC

Input Format
Số nguyên dương n

Constraints
1≤n≤10^6

Output Format
Kết quả của bài toán

Sample Input 0
10

Sample Output 0
18
'''

n = int(input())

s = 0

for i in range(1, n + 1):
    if i % 3 == 0:
        s += i
print(s)
