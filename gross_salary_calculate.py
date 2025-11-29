#Input basic salary
BS=float(input("Enter your gross salary"))
#Dearness Allowance after after added
DA=((BS*40)/100)
print("Dearness Allowance is: ",DA)
#House Rent after added
HR=((BS*20)/100)
print("House rent is",HR)
#Gross Salary after calculate
total_salary=(BS+DA+HR)
print("Total gross salary is:",total_salary)

