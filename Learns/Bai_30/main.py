#Phân tích thừa số nguyên tố, duy nhất
#30 = 2 x 3 x 5
#60 = 2 x 2 x 3 x 5

import math

def pt(n):
    for i in range(2, math.isqrt(n) + 1):
        if n % i == 0:
            #i: thừa số nguyên tố
            while(n % i == 0):
                print(i , end = ' ')
                n //= i
    #N là số nguyên tố
    if n > 1:
        print(n)
        
if __name__ == '__main__':
    n = int(input())
    pt(n)