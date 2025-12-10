#-------------------- LIST ----------------------

marks = [234,564567,688,7667,464746,56,36.6,45.56,46.56,]
print(marks)
print(type(marks))

print(marks[0])
print(marks[1])
print(marks[2])
print(marks[4])

print("lengh of list is ",len(marks))

student =["Jack",673, 98251735485,"A/B road, ajgsf High stree amstabavm, ohia state", 466575]
print(student)


#--------LIST are Mutable
#------- String are Immable

str = "Jack and jonses well"
print(str)
# str[0] = "Y" #-- It will not work and not replace in string 

#But this ispossible in LIST

student [2] = 7788665555 # I have changed number 98251735485 from to 7788665555
print(student)

#list slicing ----------------

print(student [1:4]) #--> [673, 7788665555]
print(student [:2]) #--['Jack', 673]
print(student [:3]) #-- ['Jack', 673, 7788665555]

print(student [-3:-1]) #--> [7788665555, 'A/B road, ajgsf High stree amstabavm, ohia state']
print(student [-4:]) #--> [673, 7788665555, 'A/B road, ajgsf High stree amstabavm, ohia state', 466575]



