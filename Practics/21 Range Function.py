
# -----------------------------------  range( ) -------------------------------
# Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number.
# rangel start?, stop, step?)

print(range(5))

seq = range(10)
for el in seq:
    print(el)
print("Above code using range difrently")
# -------------------------------------------

for el in range(7):
    print(el)

print("below code using start and stop")
for el in range(9,13):
    print(el)

print("below code using start, stop and step")
for el in range(7,35,5):
    print(el)



    # Print numbers from 1 to 100.




# Print numbers from 100 to 1.

print("below code using start, stop and step")
for el in range(20,0,-1):
    print(el)

# Print the multiplication table of a number n.

n = int(input("enter number : "))
for i in range (1, 11): 
    print(n *i)