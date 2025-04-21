list = ["krrish", "prakash", "daya", "dharmi"]

def to_upper(list) :
    return [i.upper() for i in list]

print(to_upper(list))

# Another method

def to_up(list) :
    res = []
    for i in list :
        res.append(i.upper())
    return res  
