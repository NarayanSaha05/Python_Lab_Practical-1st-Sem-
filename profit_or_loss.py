#Input subject marks
a=int(input("Enter Cost price:"))
b=int(input("Enter Selling price:"))
if a<b:
    print("The Saller has made profit")
    profit=b-a
    print("The profit is", profit)
else:
    print("The Saller has made incured Loss")
    loss=a-b
    print("The incured Loss is", loss)

