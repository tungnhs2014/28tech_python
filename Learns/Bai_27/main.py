#function'
#Tham số hình thức: Parameter
def tong(a, b):
    res = a + b
    return res

def change(n):
    n *= 2

def xinchao(name1, name2, name3):
    print('Xin chao', name1, name2, name3)

def infor(name, job = 'Xe om'):
    print(name, job)

m, n = 10, 20
print(tong(m , n)) #Đối số = tham số chính thức = Argument

#Viết hàm tính giai thừa
def gt(n):
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

#Viết hàm tính a^b
def lt(a, b):
    res = 1
    for i in range(b):
        res *= a
    return res

def tonghieu(a, b):
    tong = a + b
    hieu = a - b
    return tong, hieu

def tich(a, b):
    return 100

#Code để chạy chương trình
if __name__ == '__main__':
    #code
    a = 1000
    change(a) #gán a cho n => n = 1000
    print(a)
    xinchao('X', 'Y', 'Z') #Positional argument
    xinchao(name3= 'Teo', name2= 'Ty', name1= 'Nam') #keyword argumemt
    infor('28tech', 'Developer')
    infor('Teo') #Default argument
    print(gt(10))
    print(lt(2, 10))
    # t, h = tonghieu(10, 20)
    print(tonghieu(10, 20))
    print(tich(10, 20))

