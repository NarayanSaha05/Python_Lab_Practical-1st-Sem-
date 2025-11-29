s = input("Enter a string: ")
print("Characters with odd frequency:")
newstr=""
for ch in s:
    freq = 0
    for c in s:
        if ch == c:
            freq += 1
    if freq % 2 != 0:
        if ch not in newstr:
            newstr+=ch

print(newstr)
