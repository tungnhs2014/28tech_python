#Lý thuyết đồng dư
#(A + B) % C = ((A % c) + (B % C)) %C
#(A - B) % C = ((A % c) - (B % C)) %C
#(A * B) % C = ((A % c) * (B % C)) %C
#(A / B) % C = ((A % c) * (B^-1 % C)) %C
#Tính N! chia dư cho 10^9 + 7
#Khi bài toàn yêu cầu chia dư kết quả cho 1 số nào đó => Tính đến đâu chia dư đến đó
#Tính a^b chia dư cho c

import math

if __name__ == '__main__':
    a, b, c = map(int, input().split())
    res = 1
    for i in range(b):
        res *=a
        res %=c
    print(res)

    