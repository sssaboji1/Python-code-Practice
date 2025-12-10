# ----------------------Functions in Python-----------------------------
# Block of statements that perform a specific task.
# def func_ name( param 1, param2.) : K
# #some work return val
# func_ name arg1, arg2 ..) #function call

def cal_sum(a, b):    #-----------Paramaeters
    addition = a + b
    return addition

print ("The addition of 1st= ",cal_sum (2, 3))   #-------Arguments

sum = cal_sum(7, 12)
print("The addition of 2nd= ",sum)

sum = cal_sum(9, 15)
print("The addition of 3rd= ",sum)

# ---------------------------------------------------------------------------

def test():
    print("Hello")

print(test())  #---> None - because this fuction not giving any return

# ---------------------------------------------------------------------------
def cal_avg(a,b,c):
    sum = a+b+c
    avg =(sum/3)
    print(avg)
    return avg

print("Average of this:", cal_avg(5,7,10))

# -------Functions in Python-----------
#-------- 1. Built-in Functions
# print( )
# len( )
# type( )
# range( )
# ------- 2. User defined Functions

# ---------------------------------------------------------------------------

# ------------------- Default Parameters ---------------------
# Assigning a default value to parameter, which is used when no argument is passed.


def cal_prod(a=4, b=2):
    print (a * b);
    return a * b
cal_prod( )

#Single paramaeter
def cal_prod (a, b=2):
    print (a * b);
    return a * b
cal_prod (7)

# ---------------------------------------------------------------------------


# Q. WAF to print the length of a list. ( list is the parameter)
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_len(list):
    print (len (list))

print_len (cities)
print_len (heroes)

def print_list(cities):
    for item in cities:
        print(item)
print_list(heroes)

def print_list(cities):
    for item in cities:
        print(item)
print_list(cities)

# ---------------------------------------------------------------------------
# Q. WAF to print the elements of a list in a single line. ( list is the parameter)
cities = ["delhi", "gurgaon", "noida", "pune", "mumbai", "chennai"]
heroes = ["thor", "ironman", "captain america", "shaktiman"]

def print_list(cities):
    for item in cities:
        print(item, end=" ")
print_list(heroes)


def print_list(cities):
    for item in cities:
        print(item, end=" ")
print_list(cities)

# ---------------------------------------------------------------------------
# Q. WAF to find the factorial of n. (n is the parameter)
def cal_factorial(n):
    fact = 1
    for i in range(1,n+1):
        fact *= i
    print("\n","Factorial of number is",fact)

cal_factorial(5)


# ---------------------------------------------------------------------------
# Q. WAF to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val *83
    print(usd_val,"USD =",inr_val ,"INR")  

converter(5)

# ---------------------------------------------------------------------------
# Q. WAF a function for odd and even
def number(n):
    num = n%2
    if(num ==0):
        print("number",n,"is even number")
    else:
        print("number",n,"is odd number")

number(10)       

