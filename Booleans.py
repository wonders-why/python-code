# Boolean usage

varboola = 10
varboolb = "hello"
varboolc = None
varboold = 0

# Any value that is not 0, empty, or None will be True. Anything else (0, empty, None) is False.
print(bool(varboola))  # True
print(bool(varboolb))  # True
print(bool(varboolc))  # False
print(bool(varboold))  # False
print(bool(''))        # False

# Even a function returning False or 0 will have a boolean value False.

# Here is an example of a function (or module) that returns boolean values:
print(isinstance(varboola, int))  # True
print(isinstance(varboolb, int))  # False

# Comparison operators and if-else can also return boolean values.
print(7 > 9)  # False

x = 0
if x is True:
    print("The expression is true")
else:
    print("The expression is false")
