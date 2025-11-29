print("Enter 8 integers:")                    # ask user to input 8 numbers

block_count = 0                               # count total increasing blocks
current_length = 1                            # current block length
longest = 1                                   # store longest block length

# Take the first number separately
prev = int(input())                           # store first number
count = 1                                     # numbers read

while count < 8:                              # loop until 8 numbers total
    num = int(input())                        # take next number
    count += 1                                # increase input counter

    if num > prev:                            # check if increasing
        current_length += 1                   # extend current block
    else:                                     # new block starts
        block_count += 1                      # count previous block
        if current_length > longest:          # check if longest
            longest = current_length
        current_length = 1                    # reset for new block

    prev = num                                # update previous number

# Final block process
block_count += 1                              # count last block
if current_length > longest:                  # update longest if needed
    longest = current_length

print("Number of increasing blocks:", block_count)
print("Length of the longest block:", longest)


# Enter 8 integers:
# 5
# 7
# 9
# 4
# 6
# 8
# 3
# 5
