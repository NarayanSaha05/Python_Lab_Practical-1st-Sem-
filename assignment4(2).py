s = input("Enter a mixed string: ")

# Extract digits
digits = [int(ch) for ch in s if ch.isdigit()]

if not digits:
    print("No digits found")
else:
    total = sum(digits)
    avg = total / len(digits)
    max_digit = max(digits)
    min_digit = min(digits)

    print("Sum =", total)
    print("Average =", avg)
    print("Max =", max_digit)
    print("Min =", min_digit)
