# Write a program to create a csv file that we can directly open in MS-Excel.

import csv

data = [
    ["Name", "Age", "City"],
    ["John", 25, "New York"],
    ["Sophia", 30, "Los Angeles"],
    ["David", 22, "Chicago"],
    ["Emma", 28, "Houston"]
]

with open('output.csv', 'w', newline = '') as file:
    writer = csv.writer(file)
    writer.writerows(data)

print("CSV file created successfully.")