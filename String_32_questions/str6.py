s = input("Enter string: ")
mid = len(s) // 2  # middle index
ans = s[:mid] + s[mid:].upper()     # first half and second half
print(ans)