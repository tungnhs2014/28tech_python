'''
28techland là vùng đất mà cư dân cực kì thích uống bia, vì thế để tăng số lượng bia bán ra các cửa hàng bia ở đây đưa ra khuyến mại như sau: 
Cứ 3 vỏ chai bia sẽ được đổi một chai bia mới. Biết rằng ở 28techland, mỗi chai bia có giá 28 xu, nhiệm vụ của bạn là xác định với N xu cho trước, 
bạn có thể mua được tối đa bao nhiêu chai bia tính cả việc đổi thưởng bằng vỏ chai?

Gợi ý: Bước 1: Tính số lượng chai bia mua bằng tiền (n / 28). 
Sau đó làm 1 vòng lặp while với điều kiện lặp là số lượng vỏ chai mình có >= 3, bên trong vòng lặp thì tính số lượng chia bia đổi được và cập nhật vỏ chai.

Input Format
Dòng duy nhất chứa N là số đồng xu ban đầu

Constraints
1<=N<=10^6

Output Format
In ra số lượng chai bia tối đa có thể mua

Sample Input 0
138

Sample Output 0
5

Explanation 0
138 xu có thể mua được 4 chai bia, 4 vỏ chai của chai bia này sẽ đổi thêm được 1 chai bia nữa. Kết quả tổng số chai bia có thể mua là 5.
'''

n = int(input())

ans = n // 28
vo = ans

while(vo >= 3):
    temp = vo // 3
    ans += temp
    vo = vo % 3 + temp

print(ans)
