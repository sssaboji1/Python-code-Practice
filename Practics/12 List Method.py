#--------------- List Method ---------------

cricket_score = [ 7,4,9,3]
print(cricket_score)

cricket_score.append(800)
print(cricket_score)

cricket_score.reverse()
print("Reverse List:", cricket_score)

cricket_score.sort()
print(cricket_score)

cricket_score.sort(reverse=True)
print(cricket_score)

Fruit = ["Orange","Banana", "Apple" ]

Fruit.reverse()
print("Reverse List of fruit:",Fruit)

Fruit.sort()
print(Fruit)

Fruit.sort(reverse=True)
print(Fruit)

Fruit.insert(2,"Jackfruit")
print(Fruit)

Fruit.remove("Banana")
print(Fruit)

Fruit.pop(2)
print(Fruit)



#Q. Check if the list contains PALINDROME of element  [HINT use copy()mentod]


list1 = [1,2,3,4,3,2,1]

copy_list = list1.copy()
list1.reverse()

if(copy_list == list1):
    print("This is palndrom list")
else:
    print("This in not plandrom : ")

