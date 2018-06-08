def votersId():
    l1,l2,l3=map(int,input().split())
    set1=set()
    set2=set()
    set3=set()
    chosen=set()
    for i in range(l1):
        set1.add(eval(input()))
    for i in range(l2):
        set2.add(eval(input()))
    for i in range(l3):
        set3.add(eval(input()))
    chosen.update(set1&set2)
    chosen.update(set2&set3)
    chosen.update(set1&set3)
    chosen=list(chosen)
    chosen.sort()
    print(len(chosen))
    for i in range(len(chosen)):
        print(chosen[i])
 
 
 
votersId()