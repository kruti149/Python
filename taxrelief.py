income = float(input("Enter the annual income: "))
# taxrelief = 0.0
if(income <=0):
    taxrelief = 0.0
elif(income < 85528):
    taxrelief = (income * 18/100)-556.2
    print("tax relief is ", taxrelief)
else:
    taxrelief = (14839.2+((income-85528)*32/100))
    print (" else tax relief is ", taxrelief)

taxrelief = round(taxrelief, 0)
print("The tax is:", taxrelief, "thalers")
