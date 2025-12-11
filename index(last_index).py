# s = input("Enter a string: ")

# arr = []


# for i in range(len(s)):
#     if s[i]!=' ':
#         prev_index = 0
#         for j in range(i-1, -1, -1):
#             if s[j] == s[i]:
#                 prev_index = j + 1
#                 break
#         arr.append(prev_index)

# print("arr:", arr)

# s = input("Enter a string: ")

# arr = [0] * len(s)

# for i in range(0,len(s)):
#     if s[i]!=' ':
#         for j in range(i-1, -1, -1):
#             if s[i] == s[j]:
#                 arr[i]=j+1
#                 break
# print("arr:", arr)

#assignment 4(1)
s1=input("Enter the first string: ")
s2=input("Enter the second string: ")

i=0
j=len(s2)-1
result=""
while i < len(s1) and j >= 0:
    result=result+s1[i]+s2[j]
    i=i+1
    j=j-1

if len(s1) > len(s2):
    result=result+s1[i:] 
elif len(s2) > len(s1):
    result = result + s2[j::-1]   
print("The merged string is:", result)



