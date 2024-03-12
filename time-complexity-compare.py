def E(n,k):
    if k==0:
        return 0
    else:
        return E(n,k-1)*f(n,k)+f(n,k)*(f(n,k)-1)/2

def f(n,k):
    return n*w(n,k-1)+1

def w(n,k):
    if k==0:
        return 1
    else:
        return f(n,k)*w(n,k-1)



for n in range(2,9):
    for k in range(2,9):
        a = E(n,k)
        b = n*k*(n*k+pow(2,k))
        print(a)
        print(b)
        print("n="+str(n)+", k="+str(k)+":")
        if a>b:
            print("The algorithm DPC is more efficiency!")
        else:
            print("The algorithm DPC is not efficiency!")


