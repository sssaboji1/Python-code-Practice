print("Test Success")

A=2
B=5
c= A+B
sum = c
print("The addition of two number is ", c)
print("The toal ship count is ",sum)

print("My name is jack. I hav ",11,"sords on my ship")
print(10000000098232436)
print(134+2463)

name= "Jack" #String
age=24 #int
price = 198.75 #Floting 

print("My name is",name,"and gae is",age,"the price of my ship is",price)

age2=(age+5)
print(age2)
Old = False
apple = None

"""
----------------- Data Type ----------------
Integers (Whole numbers: 1,2,3, 234, 0, -234, -4546,-436)
String ("tetyy", "dsgf")
Float (356.67, 345.647)
Boolean (True, False) --> T and F shouls be capital 
None 
"""

print(type(name)) # <class 'str'>
print(type(age))  # <class 'int'>
print(type(price)) # <class 'float'>
print(type(age2)) # <class 'int'>
print(type(Old))  # <class 'bool'>
print(type(apple)) # <class 'NoneType'>




# -------ARITHMATIC OPERATORS------------
a=5;
b=3;
sum = a+b 
diff = a-b 
mult = a*b 
div = a/b 
remi = a%b # to find out REMAINDER 
powe = a**b  #a^b --> 5^3 --> 5 to the power 3= 5x5x5 = 125

print(sum,diff,mult,div,remi,powe)


#--------------------- Relational / COMPARISON OPERATORS -------------------

a = 50
b = 30
print(a == b) # --> Return should be boolen value, True or False
print(a != b)
print(a > b)
print(a >= b)
print(a < b)
print(a <= b)


#--------------------- ASSIGNMENT OPERATORS -------------------

Num = 5 # here '=' is assignment operator
# Num = Num +50 --> 120 
Num += 10 # --> 120 
print(Num)

Num -= 2 # --> 
print(Num)

Num *= 2 # --> 
print(Num)

Num /= 2 # --> 
print(Num)

Num %= 2 # --> 
print(Num)

Num **= 2 # --> 
print(Num)



#--------------------- Logical OPERATORS -------------------

# #not
# or 
# and

print(not False) # --> True
print(not True) # --> False

a=40
b=90

#-------- NOT---------

print(not (a>b)) # --> True
print(not (a<b)) # --> False


#-------- AND---------
val1 =True
val2 = False
print("Print AND oprator:", val1  and val2 ) #-> False

val1 =True
val2 = True
print("Print AND oprator:", val1  and val2 ) # --> True

#-------- OR---------
val1 =False
val2 = False
print("Print OR oprator:", val1  or val2 ) #-> False

val1 =True
val2 = False
print("Print OR oprator:", val1  or val2 ) # --> True

val1 =False
val2 = False
print("Print OR oprator:", (a==b)  or (a<b) ) # --> True



#---------------------------------------Type Conversion--------------------------------------------------
# 1. Type conversion --> Atumatcally conversion
# 2. Type Casting --> Need to do it manual Conversion

a=10 #int
b=5.5 #Flot
sum = a+b # 10+5.5 = 15.5
print(sum) #python converted atomaticaly the data type of a from int to Flot


# a="10" #string
# b=5.5 #Flot
# sum = a+b # "10"+5.5 = errr--> can only concatenate str (not "float") to str
# print(sum) #python converted atomaticaly the data type of a from int to Flot

#so wee need to do TYPE CASTING here manually to use string into int
#--------------------- Type Casting -------------------
a=int("30") #string--> but created type casting here int("30")
b=5.5 #Float
sum = a+b # "10"+5.5 = errr--> can only concatenate str (not "float") to str
print(sum) #python converted atomaticaly the data type of a from int to Flot
print(type (a))
print(a)

a=float("10") #string--> but created type casting here int("30")
b=12.5 #Float
sum = a+b # "10"+5.5 = errr--> can only concatenate str (not "float") to str
print(sum) #python converted atomaticaly the data type of a from int to Flot
print(type (a))
print(a)

