with open("file1.txt", "r") as file1, open("file2.txt", "r") as file2, open("merged.txt", "w") as merged_file:
    lines1 = file1.readlines()
    lines2 = file2.readlines()

    max_length = max(len(lines1), len(lines2))

    for i in range(max_length):
        if i < len(lines1):
            merged_file.write(lines1[i])
        if i < len(lines2):
            merged_file.write(lines2[i])

print("Files merged alternatively into 'merged.txt' successfully.")