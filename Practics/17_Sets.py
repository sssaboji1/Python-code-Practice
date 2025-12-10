 #   Set in Python

# Set in Python
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

# nums = { 1, 2, 3, 4}
# set2 = { 1, 2, 2, 2}

# #repeated elements stored only once, so it resolved to {1, 2}
# null_set = set( )
# #empty set syntax



collection = {9,4,0,1, "Hello jack", "City", 2,4, "Hello jack"}
print(collection)
print(type(collection))
print(len(collection))



collection = set() # empty set
print(type(collection))

collection = {} # Empty disctionary
print(type(collection))


# ---------- Set Methods --------------
# set.add( (el)
# #adds an element
# set.remove(el) #removes the elem an
# set.clear ) #empties the set
# set.pop() #removes a random value
# set.union( set2) #combines both set values & returns new
# set intersection( set2) #combines common values & returns new


collection = set() # empty set

collection.add(5)
collection.add(1)
collection.add("Philipines")
collection.add(1)
print(collection)

collection.remove(1)
collection.remove(5)
# collection.remove(70) # -error
print(collection)


collection.add(("new",34545,646,"Test")) # add tuple in set
print(collection)

#collection.add(["new",34545,646,"Test"]) # CAN NOT add list in set ---- TypeError: unhashable type: 'list'

print(collection.pop()) # show any random valew from set
print(collection.pop())

print(len(collection))

collection.clear()
print(collection)  # Set become empty
print(len(collection))


set1 = {1,2,3,5}
set2 = {4,5,3,2}

print(set1.union(set2)) # combination of set1 and set1 only unique values
print(set1)
print(set2)

print(set1.intersection(set2)) # common values of both set



# ----------------------Let's Practice----------------------
#Q. 1
# Store following word meanings in a python dictionary :
# table: "a piece of furniture", "list of facts & figures" cat: "a small animal"

tset_dictionary = {
"table": ["a piece of furniture", "list of facts & figures"],
"cat": "a small animal"
}

print(tset_dictionary)

#Q. 2
# You are given a list of subjects for students. Assume one classroom is required for 1 subject. How many classrooms are needed by all students.
# "python", "java", "C++", "python", "javascript",
# "java", "python", "java", "C++", "C"

test_set1  = {"python", "java", "C++", "python", "javascript"}
test_set2  = {"java", "python", "java", "C++", "C"}
print("Classrom required for each class is ", len(test_set1.union(test_set2)))



#Q. 3
# WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.





#Q. 4
# Figure out a way to store 9 & 9.0 as separate values in the set.
# (You can take help of built-in data types)





#Q. 5 Diffrence between list, Tuple, Disctionary ans SET
# How its define
# How it can be use in each other
# The limitation
# which are the imulatble and immutables in above 