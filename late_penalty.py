# Input number of days late
days = int(input("Enter the number of days late: "))

# Check fine conditions
if days <= 5:
    f=(days*0.50)
    print("Fine is ",f)
elif days <= 10:
    f=(5*0.50)+(days-5)*1
    print("Fine is ",f)
elif days <= 30:
    f=(5*0.50)+(5*1)+(days-10)*5
    print("Fine is ",f)
else:
    print("Your membership is cancelled.")
