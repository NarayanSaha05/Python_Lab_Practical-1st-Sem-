a = input("Enter first string: ")
b = input("Enter second string: ")

set_a = set(a)
set_b = set(b)

missing = set_a - set_b

if not missing:
    print("Balanced = True")
else:
    print("Balanced = False")
    print("Missing characters from a in b:", "".join(missing))