def add_digit(num):
    add = 0
    while num > 0:                     # loop to sum digits
        add += num % 10
        num = num // 10
    return add

count = 0

print("Enter positive integers one by one (0 or negative to stop):")  # show only ONCE

while True:
    num = int(input())               # take number normally (no repeated message)

    if num <= 0:                     # stop when <=0
        break

    count += 1

    iterations = 0                  # how many times digit sum is done
    digit_sum = num                 # start from original number

    while digit_sum > 9:            # loop until it becomes single digit
        digit_sum = add_digit(digit_sum)
        iterations += 1

    print("Iterations:", iterations, ", Final digit:", digit_sum)

print("Total numbers processed:", count)


# Enter positive integers one by one (0 or negative to stop):
# 9875
# Iterations: 2 , Final digit: 2
# 99
# Iterations: 1 , Final digit: 9
# 5
# Iterations: 0 , Final digit: 5
# 0
# Total numbers processed: 3