n = 500 # n global

def local_scope():
    global n
    n = 1000 #global
    print(n)

def outer():
    x = 2804
    def inner():
        nonlocal x #enclosing scope
        x = 1000
        print(x)
    inner()
    print(x)
        

if __name__ == "__main__":
    # print(n)
    # local_scope()
    # print(n)
    outer() 