'''
Cho số nguyên dương không âm N, ở mỗi thao tác bạn thực hiện tính tổng các chữ số của N sau đó gán lại cho N, 
thao tác này được thực hiện cho tới khi N chỉ còn 1 chữ số. Ví dụ N = 278 -> 17 -> 8, vậy ta có dạng rút gọn của 278 là 8. 
Nhiệm vụ của bạn là tìm dạn rút gọn của 1 số nguyên không âm N cho trước

Input Format
1 dòng chứa số N

Constraints
0<=N<=10^18

Output Format
In ra dạng rút gọn của N

Sample Input 0
999991020

Sample Output 0
3

Explanation 0
999991020 -> 48 -> 12 -> 3
'''
n = int(input())
while n >= 10:
    #Tính tổng chữ số của n => gán lại cho n
    tong = 0
    while n != 0:
        tong += n % 10
        n //= 10
    n = tong
print(n)
