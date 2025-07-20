# Traversal in simple words

tople = (1, 2, 3, 4, 5)

print("It's a for-each loop")
for x in tople:
    print(x)

print("It's a range function")
for x in range(1, len(tople) + 1):  # or use range(len(tople)) for 0-based indexing
    print(x)

print("It's a while loop")
x = 0
while x < len(tople):
    print(tople[x])
    x += 1
