# While

i = 1
while i <= 5:   
    print("This is" , i , "number")
    i+=1
print("Loop ended")


#------------------------------- Let's Practice --------------------------

# Print numbers from 1 to 100.
i= 1
while i <= 100:
    print(i)
    i+=1

# Print numbers from 100 to 1.
i=100
while i >=1:
    print(i)
    i-=1

# Print the multiplication table of a number n.

num = int(input("Enter a number:"))
i=1
while i<=10:
    table =(num * i)
    print(table)
    i+=1
print("table end") 


# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

data = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]
lendata =len(data)
i = 0;
while i<lendata:
    print(data[i])
    i+=1
print("end lsit + ve")

j = (lendata -1)
while j>0:
    print(data[j])
    j-=1
print("end lsit -ve")


# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
#-------- Concept of Contine and Break ------------------
