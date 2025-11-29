s = input("Enter a string: ")
i = j = count = 0
for char in s:
    if char == ' ':
        count += 1
words = ["" for _ in range(count + 1)]
for char in s:
    if char == ' ':
        j += 1
    else:
        words[j] += char
result = ""
for w in words:
    if len(w) == 1:
        result += chr(ord(w[0]) - 32) + " "
    else:
        result += chr(ord(w[0]) - 32) + w[1:-1] + chr(ord(w[-1]) - 32) + " "
print("Result:", result)
