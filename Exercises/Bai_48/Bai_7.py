'''
Cho 2 số nguyên dương N và K. Hãy tính tổ hợp chập K của N. 
Tiện thể các bạn ôn lại một vài tính chất của tổ hợp chập K của N nhé.

Input Format
2 số nguyên dương N và K.

Constraints
0≤k≤n≤10.

Output Format
Kết quả của tổ hợp chập K của N.

Sample Input 0
10 2

Sample Output 0
45
'''

def tohop(n, k):
    if k == 0 or k == n:
        return 1
    return tohop(n -1, k -1) + tohop(n -1, k)

if __name__ == '__main__':
    n, k = map(int, input().split())
    print(tohop(n, k))