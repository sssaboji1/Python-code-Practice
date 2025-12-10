#--------------------CONDITINAL Statments--------------------

Age = int(input("Please provide your age : "))

if(Age > 18):
    print("You are applicable for apply for voter Id")
if(Age > 18):
     print("You are applicable for apply for Driving License")
elif (Age ==18):
    print("You can Apply for voter ID for next month")
else:
    print("You Can NOT apply for VOTER ID")

print("End of code")

#----- INDENTATION is empty space of code: in above code it used before print condition


marks = int(input("Enter your marks: "))

if(marks >= 90):
    grade = "A"
elif(marks<90 and marks >= 80):
    grade = "B"
elif(marks <80 and marks >=70):
    grade = "C"
elif(marks<70 and marks >= 60):
    grade = "D"
else:
    grade = "F"
print("Your grade is ",grade)

