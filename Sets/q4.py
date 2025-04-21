# A set contains names which begin either with A or with B. Write a program to separate out the names into two sets, one containing names beginning with A and another with B.

name = {"aditya", "bhushan", "abhay", "bhagya", "anil", "babubhai"}

def seperate_names(name) :
    A_name = set()
    B_name = set()
    
    for i in name :
        if i[0] == "a" or i[0] == "A" :
            A_name.add(i)
        elif i[0] == "b" or i[0] == "B" :
            B_name.add(i)

    return A_name, B_name

A_name, B_name = seperate_names(name)   
print("The set of names beginning with A is: ", A_name)
print("The set of names beginning with B is: ", B_name)