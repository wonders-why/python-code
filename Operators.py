# Arithmetic operators
a = 10
b = 3

print(a + b)      # 13 → addition
print(a - b)      # 7 → subtraction
print(a * b)      # 30 → multiplication
print(a / b)      # 3.333... → true division
print(a % b)      # 1 → modulus (remainder)
print(a ** b)     # 1000 → exponentiation (10^3)
print(f"{a // b:.2f}")  # 3.00 → floor division, formatted to 2 decimals

# Assignment operators
x = 5
x += 3     # x = 8
print(x)

x -= 2     # x = 6
print(x)

x *= 4     # x = 24
print(x)

x /= 3     # x = 8.0
print(x)

x %= 3     # x = 2.0
print(x)

x **= 2    # x = 4.0
print(x)

x //= 2    # x = 2.0
print(x)

# Comparison operators
print(a == b)   # False → equal
print(a != b)   # True → not equal
print(a > b)    # True → greater
print(a < b)    # False → less
print(a >= b)   # True → greater or equal
print(a <= b)   # False → less or equal

# Logical operators
print(a > 5 and b < 5)   # True → both true
print(a > 5 or b > 5)    # True → at least one true
print(not(a > 5))        # False → reverse

# Identity operators
c = [1, 2, 3]
d = c
e = [1, 2, 3]

print(c is d)        # True → same object
print(c is e)        # False → different objects, same contents
print(c is not e)    # True → not the same object

# Membership operators
print(2 in c)        # True → 2 in list
print(4 not in c)    # True → 4 not in list

# Bitwise operators
m = 5      # 0101
n = 3      # 0011

print(m & n)    # 1 → AND: 0101 & 0011 = 0001
print(m | n)    # 7 → OR:  0101 | 0011 = 0111
print(m ^ n)    # 6 → XOR: 0101 ^ 0011 = 0110
print(~m)       # -6 → NOT: flips all bits
print(m << 1)   # 10 → left shift: 0101 → 1010 (multiply by 2)
print(m >> 1)   # 2 → right shift: 0101 → 0010 (divide by 2)


# the biwise operatos are useless for now and for future too, most of the time so no need to pay attention unless u really need to.