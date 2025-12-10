#--------------- TUPLES----------------

# List --> Mutable data type
# Tuple -->  Immutable data type jus like string

city = ("New york","London","Ohio","Beging","Ohio","Ohio")
print(type(city))  # <class 'tuple'>

print(city.count("Ohio"))

print(city[0])
print(city[1])
print(city[2])

#city[2]= "Delhi" --> It will not work becaus it it Immutable

laptop = (1)
print(type(laptop)) # <class 'int'>

laptop = ("Hp")
print(type(laptop)) # <class 'str'>

laptop = (1+2)
print(type(laptop)) #<class 'int'>

laptop = (1,) #--> NEE TO USE "," Comma to consider this as tuple
print(type(laptop)) # <class 'tuple'>


#------------- SLICING IN TUPLE-----------

print(city[0:2])

print(city[-3:-1])


#Q 1. enter name of moveand store in the list
Box_office = []
movie1 = input("Enter first mobie name :")
movie2 = input("Enter second movie name : ")
movie3 = input ("Enter thired movie anme :")

Box_office = [movie1,movie2,movie3]
print("Here is the list of your movie :",Box_office)
print(type(Box_office))
print(len(Box_office))


#-------------------------- OR --------------------------
Movies = []
Movies.append(input("Enter first movie name :"))
Movies.append(input("Enter second movie name : "))
Movies.append(input ("Enter thired movie anme :"))

print(Movies)