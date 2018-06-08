def hello():
    tc=int(input())
    while tc:
        d,u,n=map(float,input().split())
        min=d*u
        best=0
        for i in range(int(n)):
            m,r,c=map(float,input().split())
            tot=(c/m)+(u*r)
            if tot<min:
                min=tot
                best=i+1
        print(best)
        tc-=1