'''
Cho số nguyên dương N. Bạn được thực hiện 3 thao tác sau đây: 1. Lấy N chia cho 2 nếu N chia hết cho 2. 2.
Lấy N chia hết cho 3 nếu N chia hết cho 3. 3. Giảm N đi 1 đơn vị. Hãy đếm số thao tác ít nhất để biến đổi N về 1.

Input Format
Số nguyên dương N.

Constraints
1≤n≤50

Output Format
In ra số thao tác tối thiểu cần thực hiện.

Sample Input 0
38

Sample Output 0
5

Explanation 0
Giải thích test : 1. N = N / 2 = 19 2. N = N - 1 = 18 3. N = N / 3 = 6 4. N = N / 2 = 3 5. N = N / 3 = 1
'''

def F(n):
    if n == 1:
        return 0
    tt1, tt2, tt3 = 10 ** 9, 10 ** 9, 10 ** 9
    if n % 2 == 0:
        tt1 = 1 + F(n // 2)
    if n % 3 == 0:
        tt2 = 1 + F(n // 3)
    if n > 1:
        tt3 = 1 + F(n -1)
    return min(tt1, tt2, tt3)
        
        
if __name__ == '__main__': 
    n = int(input())
    print(F(n))
