str=input("Enter a string:")
len = 0
for i in str:
    if i != ' ':
        len += 1
print("len of the string (ignore spaces):", len)