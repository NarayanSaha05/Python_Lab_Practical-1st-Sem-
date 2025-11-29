s1 = input("Enter first string:")
s2 = input("Enter Second string:")

result = ""     

c1 = 0
for i in s1:
    c1 += 1

c2 = 0
for i in s2:
    c2 += 1

limit = c1
if c2 < c1:
    limit = c2

for k in range(limit):
    result = result + s1[k]
    result = result + s2[c2 - 1 - k]

for k in range(limit, c1):
    result = result + s1[k]

for k in range(c2 - limit - 1, -1, -1):
    result = result + s2[k]

print(result)