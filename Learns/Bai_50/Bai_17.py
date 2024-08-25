'''
Cho một số nguyên không âm N, hãy in ra N theo thứ tự các chữ số từ trái qua phải và từ phải qua trái. 
Chú ý phải sử dụng hàm đệ quy cho cả 2 yêu cầu.

Input Format
Số nguyên không âm N.

Constraints
0≤n≤10^18

Output Format
Dòng đầu tiên in ra các chữ số của n theo thứ tự từ trái qua phải. 
Dòng thứ hai in ra các chữ số của n theo thứ tự từ phải qua trái. Các chữ số được viết cách nhau một dấu cách.

Sample Input 0
21218

Sample Output 0
2 1 2 1 8 
8 1 2 1 2 
'''


def in1(n):
    if n < 10:
        print(n, end = ' ')
    else:
        print(n % 10, end = ' ')
        in1(n // 10)

def in2(n):
    if n < 10:
        print(n, end = ' ')
    else:
        in2(n // 10)
        print(n % 10, end = ' ')

if __name__ == '__main__':
    n = int(input())
    in2(n)
    print()
    in1(n)