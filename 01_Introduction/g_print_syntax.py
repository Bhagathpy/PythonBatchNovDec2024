"""
Purpose: print() function syntax and usage
    Escape Sequences
        - characters whose presence is felt, but they were not print

        \t - tab space
        \n - new line
        \b - overwrites new character

        r'' - raw string

"""

print("hello world python")
print("hello \tworld \tpython")  #using tab space
print("hello \tworld \tpython")  # using new line & tab space


# To ignore the escape sequences
print()
print("hello \tworld \\tpython")
print(r"hello \tworld \tpython")

print("C:\my\newfolder")
print(r"C:\my\newfolder")

# print(data, sep =' ', end = '\n')

print("hello")  #default end='\n'
print("world")

print("hello", end="\n")
print("world", end="\n")

print("hello" , end="___")
print("world") # default end='\n'

print("hello", end="\t")
print("world")

print()
print("hello", "world" , 12345, end="\t") # default sep=" "
print("simple") # default end='\n'

print("hello", "world" , 12345, end="\t", sep=";")
print("simple")


