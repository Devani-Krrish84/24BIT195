def compute(end) :
    
    arr = []

    for i in range(1, end+1) :
        arr.append((i, i**2, i**3))

    return arr

print(compute(5))