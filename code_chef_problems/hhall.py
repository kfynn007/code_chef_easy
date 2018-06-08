def hhall():
    tc=int(input())
    while tc:
        string=input().strip('\n')
        if string==string[::-1]:
            print(1)
        else:
            print(2)
        tc-=1
 