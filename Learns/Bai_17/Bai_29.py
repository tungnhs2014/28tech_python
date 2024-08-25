'''
Cho 4 số a, b, c, d. Hãy kiểm tra xem 4 số này có thể theo thứ tự tạo thành 1 cấp số nhân với công bội nguyên theo đúng thứ tự a, b, c, d hay không?

Gợi ý : Tìm công bội (b / a) nếu b chia hết cho a, sau đó lấy b nhân công bội và so sánh vs c, c nhân công bội và so sánh vs d.

Input Format
1 dòng chứa 4 số a, b, c, d.

Constraints
1<=a,b,c,d<=10^6

Output Format
In ra YES nếu 4 số a, b, c, d tạo thành 1 câp số nhân, ngược lại in ra NO.

Sample Input 0
92 92 92 92

Sample Output 0
YES
'''

a, b, c ,d = map(int, input().split())
if b % a == 0:
    q = b // a
    if b * q == c and c * q == d:
        print('YES')
    else:
        print('NO')
else:
    print('NO')