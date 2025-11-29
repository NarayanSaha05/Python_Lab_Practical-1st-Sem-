# s = input("Enter a string: ")
# i = int(input("Enter the character potion to remove: "))
# v = s[:i-1] + s[i:]      #use slice
# print("String after removing the character:", v)

s = input("Enter string: ")
i = int(input("Enter index to remove: "))
s1=s[:i]+s[i+1:]
print(s1)
