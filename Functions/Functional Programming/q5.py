# A list contains names of Faculty Members. Write a program to filter out those names whose length is more than 8 characters.

lst = ['John Doe', 'Jane Smith', 'Alice Johnson', 'Bob', 'Charlie Black', 'David', 'Eve Green']

ans = list(filter(lambda x: len(x) > 8, lst))
print(ans)