n = int(input("Enter how many numbers you want to enter:"))
expect_even = True
numbers = ""
for i in range(n):
    num = int(input("Enter no.: "))
    if expect_even:
        if num % 2 == 0:
            numbers = numbers + str(num) + " "
            expect_even = False
    else:
        if num % 2 != 0:
            numbers = numbers + str(num) + " "
            expect_even = True
print(numbers)
