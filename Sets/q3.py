# Create an empty set. Write a program that adds five new names to this set, modifies one existing name and deletes two names from it.

name = set()
print(name)
name.add("krrish")
name.add("daya")
name.add("prakash")
name.add("dharmi")
name.add("prabha")
print(name)
name.remove("krrish")
name.remove("daya")
print(name)