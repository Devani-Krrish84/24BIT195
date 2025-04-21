string = input("Enter a string: ")

def count_frequency(string) :
    frequency = {}

    for char in string :
        if char in frequency :
            frequency[char] += 1
        else :
            frequency[char] = 1
    
    return frequency

print(count_frequency(string))