def convert(input_string):
    words = input_string.split()
    unique_words = sorted(set(words))
    return " ".join(unique_words)

input_string = input("Enter a sequence of whitespace-separated words: ")
result = convert(input_string)
print(result)