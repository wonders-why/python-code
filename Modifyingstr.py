# Modifying strings using uppercase, lowercase, whitespace, replace, split

varstring = "hello, WORLD"
print(varstring)

# Convert to uppercase
print(varstring.upper())

# Convert to lowercase
print(varstring.lower())

# Remove leading and trailing whitespaces (here, no extra whitespace, so no visible change)
print(varstring.strip())

# Replace characters (⚠️ IMPORTANT: you must assign or print directly, as strings are immutable!)
print(varstring.replace("h", "w"))

# Split string at comma
print(varstring.split(","))

# Loop through each character
for x in varstring:
    print(x)

# Concatenation of strings
a = "poke"
b = "mon"
print(a + b)

# Formatting float value
num = 8
print(f"HI, the float value conversion from 8 to 8.0: {num:.1f}")
