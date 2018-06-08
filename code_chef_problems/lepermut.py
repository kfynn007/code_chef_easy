def elephantPerm():
    from itertools import combinations
    tc=eval(input())
    while tc:
        inversions=0
        locInversions=0
        size=eval(input())
        array=[eval(x) for x in input().split()]
        if len(array)==1:
            print ('YES')
        else:
            pairs=set(combinations(array,2))
            for pair in pairs:
                j=max(pair)
                i=min(pair)
                if j>i:
                    if array[i-1]>array[j-1]:
                        inversions+=1
            for x in range(size-1):
                if (array[x]>array[x+1]) and (array[x]>1) and (array[x]<size+1):
                    locInversions+=1
            if (inversions==locInversions):
                print ('YES')
            else:
                print('NO')
        tc-=1