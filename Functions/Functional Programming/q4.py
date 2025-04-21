# Consider the following list:

# lst = ['madam','Python',"malayalam",12321]

# Write a program to print those strings which are palindromes.

lst = ['madam','Python',"malayalam",12321]

palindrome = list(filter(lambda x: str(x).upper() == str(x).upper()[::-1], lst))
print(palindrome)