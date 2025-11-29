a=int(input("Enter your values"))
sum_of_even=0
sum_of_odds=0
for i in range(a):
    num=int(input("Enter no.:"))
    if num % 2==0:
        sum_of_even+=num
    else:
        sum_of_odds+=num
        
print("Even sum", sum_of_even)
print("Odd sum", sum_of_odds)
    
    
