'''
Bizon the Champion gần đây đã có một món quà - một tủ kính mới với n kệ và anh quyết định đặt tất cả những món quà của mình ở đó. 
Tất cả các món quà có thể được chia thành hai loại: huy chương và cúp. Bizon the Champion có a1 cúp giải nhất, a2 cúp giải nhì và a3 cúp giải ba. 
Bên cạnh đó, anh có b1 huy chương giải nhất, b2 huy chương giải nhì và b3 huy chương giải ba. Đương nhiên, phần thưởng trong tủ phải sắp xếp cho thật đẹp, 
đó là lý do Bizon the Champion quyết định tuân theo các quy tắc: bất kỳ kệ nào cũng không thể chứa cả cúp và huy chương cùng một lúc; 
không có kệ có thể chứa nhiều hơn 5 cúp; không có kệ có thể có hơn 10 huy chương. 
Giúp Bizon the Champion tìm hiểu xem có thể đặt tất cả các phần thưởng để tất cả các điều kiện được đáp ứng hay không.

Gợi ý : Tính tổng số cúp => tìm số kệ đựng cúp (chia hết cho 5 hay ko), ví dụ 12 cúp => 3 kệ, 10 cúp => 2 kệ
Tính tổng số huy chương => tìm kệ đựng huy chương (chia hết cho 10 hay ko)

Nếu tổng kệ <= n thì in YES

Input Format
Dòng đầu tiên chứa các số nguyên a1, a2 và a3. Dòng thứ hai chứa các số nguyên b1, b2 và b3 (0 ≤ b1, b2, b3<= 100). Dòng thứ ba chứa số nguyên n. Các số trong các dòng được phân tách bằng khoảng trắng đơn.

Constraints
0 ≤ a1, a2, a3<= 100; 1 <=n <=100;

Output Format
In "YES" (không có dấu ngoặc kép) nếu tất cả các phần thưởng có thể được đưa lên kệ theo cách được mô tả. Nếu không, hãy in "NO" (không có dấu ngoặc kép).

Sample Input 0
46 76 52 40 60 67 
11

Sample Output 0
NO
'''

a1, a2, a3, b1, b2, b3 = map(int, input().split())
n = int(input())

cup = a1 + a2 + a3
hc = b1 + b2 + b3
ke1, ke2 = 0, 0

if cup % 5 == 0:
    ke1 = cup // 5
else:
    ke1 = cup // 5 + 1
if hc % 10 == 0:
    ke2 = hc // 10
else:
    ke2 = hc // 10 + 1
if ke1 + ke2 <= n:
    print('YES')
else:
    print('NO')