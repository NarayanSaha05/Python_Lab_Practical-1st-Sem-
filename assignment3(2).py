n = int(input("How many values you want to enter: "))   # total inputs
k = int(input("Enter k: "))                             # divisor
nums = ""                                               # store result

for i in range(n):
    num = int(input("Enter number: "))                  # take number
    if i == 0:                                          # skip only the 1st entered number
        continue
    if num % k == 0:                                    # check divisible by k
        nums = nums + str(num) + " "                    # add number

print("The value is", nums)                             # display divisible numbers


# 9 → first input → skipped
# 12 → divisible → added
# 7 → not divisible
# 15 → divisible → added
# 18 → divisible → added