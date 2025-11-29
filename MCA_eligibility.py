a=input("Are you Graduate?(Yes=y or No=n): ")
d = input("HS or Graduate math percen you want to mention: ")
b=int(input("What is your percentage: "))
c=input("Choose your cast(sc/st/gen): ")

if a == "y":
    if d == "HS" or d == "hs" or d == "Graduate" or d == "graduate":
        if c == "sc" or c == "st":
            if b>=45 and b<=100:
                print("You r eligible")
            else:
                print("You are not eligible.......")
        else:
            if b>=50 and b<=100:
                print("you r eligible")
            else:
                print("You are not eligible....")
else:
    print("You r not eligible......")
