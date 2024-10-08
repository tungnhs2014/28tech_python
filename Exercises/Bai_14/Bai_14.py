'''
Yêu cầu: Cho biết điểm kiểm tra Tin học của 1 em học sinh (2 con điểm hệ số 1, 1 con điểm hệ số 2, 1 con điểm hệ số 3). 
In ra Kết quả học tập môn Tin học của em đó. Nếu điểm tổng kết >=8 đạt kết quả Giỏi, <8 và >=6,5 đạt kết quả Khá, <6,5 và >=5 
đạt kết quả Trung Bình, <5 đạt kết quả Yếu.
Gợi ý : ĐTB = tổng (điểm * hệ số) / (tổng hệ số)

Input Format
Một dòng chứa 4 số điểm của học sinh.

Constraints
Điểm là số thực từ 0 tới 10.

Output Format
Kết quả học tập môn Tin học của em học sinh ở dạng in hoa không dấu

Sample Input 0
9 8 7 8.5

Sample Output 0
GIOI

Sample Input 1
5 7 6.5 5

Sample Output 1
TRUNG BINH
'''

a, b, c, d = map(float, input().split())

tb = (a + b + c*2 + d*3) / 7

if tb >= 8: print('GIOI')
elif tb \
     >= 6.5: print('KHA')
elif tb >= 5:
    print('TRUNG BINH')
else: print('YEU')