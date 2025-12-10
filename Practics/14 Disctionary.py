#--------------------- DISCTIONARY is MUTABLE- changable- we cna chnge valu add edit

info = {
    "key" : "value",
    "name" : "Jack",
    "Contact": 2345234873,
    "address" : "Am/ Ohio, Wilgotr",
    "age": 22,
    "is_adult" : True,
    "subjects": ["python","c","java",".net"], # This is list
    "topics": ("dict","set"), # this is TUPLE
    "marks" : 89.37,
    12.45:33,
    2:123,
    3: "144 Clubhouse, Palm Lakes Estate, Finchley Manor, KwaDukuza 4420, South Africa"
}

print(info)

print(type(info)) #---- <class 'dict'>
print(info["subjects"])
print(info["topics"])
#print(info["cricket"]) #-- Error- no key found for this
 
info["name"] = "Will Smith" # value checnged for name from "jack" to "Will smith"

print(info)

info["name"] = "Jackson" # value checnged for name from "Will smith" to "Jackson"
info["surname"] = "Strahrdkos" # added surnmae new key with value 'Strahrdkos'

print(info)


#creating empty dictonary

empty_dicto ={}

print(empty_dicto)