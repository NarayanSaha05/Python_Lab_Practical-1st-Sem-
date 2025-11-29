#overtime paying
#taking num of hours of overtime as input
c=1
while c<11:
    h=int(input("enter your extra hour worked time"))
    if(h>40):
        extra=h-40
        pay=extra*12
        print("Enter money you get", pay)
    else:
         print("you will not get extra money")
    c+=1;
