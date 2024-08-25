'''
Doremon muốn leo lên một cầu thang gồm n bước. Anh ta có thể leo 1 hoặc 2 bước mỗi lần di chuyển. 
Doremon muốn số lần di chuyển là bội số của một số nguyên m. Số lượng di chuyển tối thiểu làm cho anh ta leo lên đỉnh cầu thang thỏa mãn điều kiện của anh ta là gì?

Gợi ý : Tìm số bước di chuyển tối thiểu (n / 2 ?) để lên cầu thang và số bước di chuyển tối đa (n) cần lên cầu thang n bậc. Gọi lần lượt là x và y,
bài toán quay về tìm số nhỏ nhất >= x và <= y chia hết cho m. Có thể dùng công thức (x + m - 1) / m * m để tìm nhanh kết quả rồi so sánh với y.

Input Format
Dòng đơn chứa hai số nguyên cách nhau n, m

Constraints
1<=n,m<=10^9

Output Format
In một số nguyên duy nhất - số lượng di chuyển tối thiểu là bội số của m. Nếu không có cách nào anh ta có thể leo lên thỏa mãn điều kiện in - 1.

Sample Input 0
10 2

Sample Output 0
6
'''

n, m = map(int, input().split())
min_step, max_step = 0, n
if n % 2 == 0:
    min_step = n // 2
else:
    min_step = n // 2 + 1
ans = (min_step + m - 1) // m * m
if ans <= max_step:
    print(ans)
else:
    print(-1)