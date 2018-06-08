def pemit():
    import itertools
    tc=int(input())
    while tc:
        n=int(input())
        arr=(x for x in range(1,n+1))
        permList=tuple(itertools.permutations(arr))
        good=[]
        for set in permList:
            cnt=0
            for i in range(len(set)):
                if set[i]!=i+1:
                    cnt+=1
            if cnt==len(set):
                good.append(set)
        selected=good[0]
        for i in range(1,len(good)):
            possible=good[i]
            if possible<selected:
                selected=possible
        for i in range(len(selected)):
            if i<len(selected)-1:
                print(selected[i],end=' ')
            else:
                print(selected[i])
 
        tc-=1
 