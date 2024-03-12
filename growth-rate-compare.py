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
        a1 = E(n,k)/E(n-1,k)-1
        b1 = (n*k*(n*k+pow(2,k)))/((n-1)*k*((n-1)*k+pow(2,k)))-1
        a2 = E(n, k) / E(n, k-1) - 1
        b2 = (n * k * (n * k + pow(2, k))) / (n * (k-1) * (n * (k-1) + pow(2, k-1))) - 1
        print(a1)
        print(b1)
        print(a2)
        print(b2)
        print("n="+str(n)+", k="+str(k)+":")
        if a1>b1 and a2>b2:
            print("The algorithm DPC is sublinear!")
        else:
            print("The algorithm DPC is not sublinear!")

