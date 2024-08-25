#Số thuận nghịch, đỗi xứng, palindrome: 1221, 123321, 1111, 131,...

def palindrome(n):
    init = n
    tmp = 0 
    while(n !=0):
        tmp = tmp * 10 + n % 10
        n //= 10
    return tmp == init
    
#code
if __name__ == '__main__':
    n = int(input())
    print(palindrome(n))