# Nested Dictonary

students = {
    "name" : "jack",    # - key - name     | value jack
    "surname" : "Willson",
    "subject": {
        "chem" : 98,
        'phy' : 95,
        '''Math''' : 100
    }
}

print(students)  # {'name': 'jack', 'surname': 'Willson', 'subject': {'chem': 98, 'phy': 95, 'Math': 100}}
print(students["surname"]) # Willson
print(students["subject"]) # {'chem': 98, 'phy': 95, 'Math': 100}
print(students["subject"]["phy"]) #95


print(students.keys()) # not return nested keys in result  only shows outer key

print(list(students.keys()))  # this make TYPECAST from disctionary to LIST.

print(len(list(students.keys())))  # LEN of disctionary or LIST. 

print(students.values())

print(list(students.values())) # this make TYPECAST from disctionary to LIST.

print(len(list(students.values()))) # this make TYPECAST from disctionary to LIST.


print(students.items())  # disctionary retuns vale of tuple

print(list(students.items()))

pairs_data = (list(students.items()))

print(pairs_data[0])
print(pairs_data[2])


print(students["name"])   # -- jack
print(students.get("name")) #--  jack

print(students.get("name2")) #-- no error only none
#print(students["name2"])   # -- retun a error



students.update({
    "contact" : 141234567890,
    "Name" : "Name NOT update due to case sensetive key name",
    "name" : "Name update from Jack to JackyChain"

})
print(students)


new_student_disct = {
    "city" : "New York",
    "sport"  : "Foosball"
}
print(new_student_disct)
students.update(new_student_disct)
print(students)

