'''
Cho 2 số x, y. Nhiệm vụ của bạn là tính x ^ y
Gợi ý : x^y sẽ không có phần lẻ thập phân vì x, y đều nguyên. Hàm pow trả về double nên bạn không được in ra luôn cout << pow(x, y). 
Với kết quả nhỏ thì không sao nhưng nếu kết quả lớn nó sẽ in ra dạng số thực, bạn thử cout << pow(10, 10) để xem thử kết quả. 
Cách làm đó là ép pow sang long long trước khi in hoặc lưu pow(x, y) vào 1 số nguyên long long rồi in ra.

int main(){
    //Nhap x y
    //Khai bao bien số nguyên kq = pow(x, y)
    //In ra biến kq
}
Input Format
1 dòng chứa 2 số nguyên dương x, y viết cách nhau một dấu cách

Constraints
1<=x,y<=12;

Output Format
In ra x^y, nếu x^y có phần thập phân thì in ra 2 số sau dấu phẩy, nếu không có phần thập phân thì không cần in.

Sample Input 0
2 2

Sample Output 0
4

Sample Input 1
4 1

Sample Output 1
4

'''
import math

x, y = map(int, input().split())
z = math.pow(x, y)
print((int)(z))
