#["eat", "tea", "tan", "ate", "nat", "bat"]
#eat tea tan ate nat bat


s = input("Enter words separated by space: ").split()

groups = {}

for w in s:
    key = ''.join(sorted(w))
    groups.setdefault(key, []).append(w)

result = list(groups.values())

print("Grouped anagrams:", result)