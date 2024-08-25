'''
Năm mới sắp đến và bạn rất hào hứng muốn biết còn lại bao nhiêu phút trước Tết. 
Bạn biết rằng hiện tại đồng hồ hiển thị h giờ và m phút, trong đó 0≤hh <24 và 0≤mm <60. 
Chúng tôi sử dụng định dạng thời gian 24 giờ! Nhiệm vụ của bạn là tìm số phút trước Tết. 
Bạn biết rằng năm mới đến khi đồng hồ hiển thị 0 giờ và 0 phút.

Gợi ý : lấy số phút trong 1 ngày - số phút đã trôi qua tới h giờ, m phút

Input Format
2 số nguyên không âm h và m.

Constraints
0≤h <24; 0≤m <60;

Output Format
In ra đáp án của bài toán

Sample Input 0
23 0

Sample Output 0
60
'''
h, m = map(int, input().split())

phut_1_ngay = 60*24
phut_ht = h*60 + m

print(phut_1_ngay - phut_ht)