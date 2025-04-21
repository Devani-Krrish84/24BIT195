def genrate_putho_triplet(limit) :
    for a in range(1, limit + 1) : 
        for b in range(a, limit + 1) :
            for c in range(b, limit + 1) :
                if a**2 + b**2 == c**2 :
                    print(f"( {a}, {b}, {c} )")

limit = int(input("Enter the limit : "))
genrate_putho_triplet(limit)