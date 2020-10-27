hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# put your code here
mins = mins + dura
updatedhr = mins // 60
print ("updated hour value is ", updatedhr)

updatedmin = mins % 60
print ("updated min values is", updatedmin)

newhr = hour + updatedhr
finalhr = newhr % 24
print("final hr", finalhr)


print (finalhr, updatedmin, sep=":")