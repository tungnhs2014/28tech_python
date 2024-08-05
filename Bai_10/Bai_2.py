'''
Đề bài yêu cầu bạn nhập : Dòng 1 là số nguyên X, dòng 2 là số nguyên Y, dòng 3 là kí tự C, dòng 4 là số thực float F, dòng 5 là số thực double D. 
Nhiệm vụ của bạn là in ra 5 dòng. Dòng 1 in X, dòng 2 in Y, dòng 3 in C, dòng 4 in F với 2 số đằng sau dấu phẩy, dòng 5 in D với 9 số sau dấu phẩy.

Gợi ý : Chú ý dùng fixed vs setprecision để in ra F và D cho chính xác, Y cần là số long long nếu không sẽ bị tràn dữ liệu và không lưu được.

int main(){
    //Khai báo 5 biến x y c f d
    //In ra x
    //In ra y
    //In ra c
    //In ra f sử dụng fixed và setprecision
    //In ra d sử dụng fixed và setprecision
}
Input Format

5 dòng lần lượt là X, Y, C, F, D

Constraints

-10^9<=X<=10^9; -10^18<=Y<=10^18; C là kí tự in hoa hoặc in thường; -10^6<=F<=10^6; -10^9<=D<=10^9;

Output Format

In ra 5 dòng theo yêu cầu

Sample Input 0

614
999999999999990528
G
19.088
2.9648
Sample Output 0

614
999999999999990528
G
19.09
'''
x = int(input())
y = int(input())
c = input()
f = float(input())
d = float(input())

print(x)
print(y)
print(c)
print('%.2f' %f)
print('%.9f' %d)
