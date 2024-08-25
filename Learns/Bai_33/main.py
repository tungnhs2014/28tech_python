#Tổ hợp chập k của N
import math

def tohop(n, k):
    return math.factorial(n) // (math.factorial(k) * math.factorial(n - k))


if __name__ == '__main__':
    a, b = map(int, input().split())
    print(math.comb(a, b))
    print(tohop(a, b))
