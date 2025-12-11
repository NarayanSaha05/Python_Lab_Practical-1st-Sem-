a = input("Enter first string: ").replace(' ', '')
b = input("Enter second string: ").replace(' ', '')

set_a = set(a)
set_b = set(b)

balanced = set_a.issubset(set_b)
#if balanced !=' ':
print("Balanced =", balanced)

if not balanced:
    missing = set_a - set_b
    print("Missing characters from a in b:", "".join(missing))