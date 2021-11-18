def boundedRatio(a, l, r):
    b = []
    for i in range(len(a)):
        if a[i] % (i + 1) != 0:
            b.append(False)
            continue
            
        x = a[i] / (i + 1)
        print(x)
        if x >= l and x <= r:
            b.append(True)
        else:
            b.append(False)
    return b

# alternative
def boundedRatio(a, l, r):
    b = []
    
    for i, v in enumerate(a):
        x = v / (i + 1)
        if int(x) == x and l <= x and x <= r:
            b.append(True)
        else:
            b.append(False)
    
    return b