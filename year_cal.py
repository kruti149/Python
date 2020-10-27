year = int(input("Enter a year: "))

if(year < 1582):
    print ("Not within the Gregorian calender period")
    
elif (((year%4) != 0) and ((year%400) != 0)):
    print ("Its common year")

else:
  print ("its a leap year")