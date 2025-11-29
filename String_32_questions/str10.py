s1 = input("Enter first string: ")
s2 = input("Enter second string: ")
seen = ""
cnt = 0
for ch in s1:
    if ch not in seen:
        seen = seen + ch
        if ch in s2:
            cnt = cnt + 1
print("Matching characters count:", cnt)
