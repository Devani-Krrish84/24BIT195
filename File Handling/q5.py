with open("source.txt", "r") as source_file:
    content = source_file.read()

content_upper = content.upper()

with open("destination.txt", "w") as destination_file:
    destination_file.write(content_upper)

print("Contents copied and converted to uppercase successfully.")