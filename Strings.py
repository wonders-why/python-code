# Strings, multiline strings, string indexing, length, and check

a = "It is a string."
b = 'It is also a string'
c = "'It is a string with quotation'"

d = """This is a multiline string.
and we can use it to output multiple lines
of code.
"""

e = "hello"

# Example of formatted print
# print(f"{e[4]}, {a}, {b}, {c}, {d}")

# Length of a string
# print(len(d))

# Checking if a word is present
# if "multiline" in d:
#     print("Multiline is there in d")
# else:
#     print("It is not there")

# if "dingdong" not in d:
#     print("It is not there")

# String slicing examples
print(d)
print(d[0:4])      # Characters from index 0 to 3
print(d[-6:])      # Last 6 characters
print(d[10:15])    # Characters from index 10 to 14
print(d[-31:-25])  # Characters from index -31 to -26
