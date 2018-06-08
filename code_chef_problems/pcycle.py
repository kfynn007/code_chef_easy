def cylic():
    import itertools
    n=int(input())
    data=[int(x) for x in input().split()]
    dataSet=set()
    dataSet.update(data)
    mainCycles=[]
    tempCycles=set()
    while  dataSet!=tempCycles:
        idx = min(dataSet - tempCycles) - 1
        pos = min(dataSet-tempCycles)
        cycles=[]
        while pos not in cycles:
            cycles.append(pos)
            pos = data[idx]
            idx = pos - 1
        cycles.append(pos)
        mainCycles.append(cycles)
        tempCycles.update(itertools.chain.from_iterable(mainCycles))
    print(len(mainCycles))
    for cycle in mainCycles:
        for idx,num in enumerate(cycle):
            if idx!=len(cycle)-1:
                print(num,end=' ')
            else:
                print(num)