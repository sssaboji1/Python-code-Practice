# Q1. write a number of odd or even provided by user

num = int(input("Enter any number : "))
if(num % 2 == 0):
    print("provided number ",num,"is even number")
else:
    print("The provided number ",num,"is odd number")


#--------------------------------------------------------------------------------

#Q.2 Find the gretest of 3 numbers provided by user
num1 = int(input("Enter 1st number : "))
num2 = int(input("Enter 2nd number : "))
num3 = int(input("Enter 3rd number : "))

if(num1>num2 and num1>num2):
    print(num1,"is the greted number")
elif(num2>num3):
    print(num2,"is the greted number")
else:
    print(num3,"is the greted number")


#--------------------------------------------------------------------------------

#Q3. number 7 multiple of 7 or not
number = int(input("Enter any number : "))

if(number%7==0):
    print("entered number is multipal of 7")
else:
    print("Enter number is NOT multipal of 7")
