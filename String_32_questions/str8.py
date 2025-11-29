# s = input("Enter a string: ")
# has_letter_number =False
# for ch in s:
#     if ch.isalnum():
#         has_letter_number = True
#         print("Contains letters and numbers")
# else:
#     print("Invalid")

# 8. Check at least one letter and one number

s = input("Enter string: ")
has_letter = False
has_digit = False
for ch in s:
    if ch.isalpha():
        has_letter = True
    if ch.isdigit():
        has_digit = True
if has_letter and has_digit:
    print("Valid- 1 letter and 1 number available")
else:
    print("Not valid")
