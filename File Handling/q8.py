with open("input.txt", "r") as input_file:
    content = input_file.read()

words_to_remove = ["a", "the", "an"]
for word in words_to_remove:
    content = content.replace(f" {word} ", " ")

with open("output.txt", "w") as output_file:
    output_file.write(content)

print("Words removed and content written to 'output.txt'.")