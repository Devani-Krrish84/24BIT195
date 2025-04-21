def frequency(input_string):
    words = input_string.split()
    freq_dict = {word: words.count(word) for word in sorted(set(words))}
    return freq_dict

input_string = input("Enter a string: ")
result = frequency(input_string)
print(result)