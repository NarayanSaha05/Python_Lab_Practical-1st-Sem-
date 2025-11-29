# Input details
health = input("Enter health (excellent/poor): ")
age = int(input("Enter age: "))
location = input("Enter location (city/village): ")
gender = input("Enter gender (male/female): ")

# Check conditions
if health == "excellent" and age >= 25 and age <= 35 and location == "city":
    if gender == "male":
        print("Person is insured.")
        print("Premium rate: Rs. 4 per thousand")
        print("Maximum policy amount: Rs. 2,00,000")
    else:
        print("Person is insured.")
        print("Premium rate: Rs. 3 per thousand")
        print("Maximum policy amount: Rs. 1,00,000")

elif health == "poor" and age >= 25 and age <= 35 and location == "village" and gender == "male":
    print("Person is insured.")
    print("Premium rate: Rs. 6 per thousand")
    print("Maximum policy amount: Rs. 10,000")

else:
    print("Person is not insured.")
