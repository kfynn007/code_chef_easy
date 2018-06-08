def palind():
    tc=int(input())
    while tc:
        txt=list(input())
        if len(txt)%2==1:
            a=txt[0:len(txt)//2]
            a.sort()
            b=txt[len(txt)//2+1:]
            b.sort()
        else:
            a = txt[0:len(txt) // 2]
            a.sort()
            b = txt[len(txt) // 2:]
            b.sort()
        if a==b:
            print('YES')
        else:
            print('NO')
        tc-=1
 