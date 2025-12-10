

# ------------------- using for ----------------------------
# Print the elements of the following list using a loop:
# [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

nums = [1, 4, 9, 16, 25, 36, 49, 64, 81,100]

for val in nums: 
    print(val)



# Search for a number x in this tuple using loop:
# (1, 4, 9, 16, 25, 36, 49, 64, 81,100)

data = (1, 4, 9, 16, 25, 36, 49, 64, 81,100,64)
x =  64 
idx = 0

for el in data:
    if(el== x):   #---- This call as LINER search
        print("number found at indix",idx)
    idx +=1


#----------- using break-----------


for el in data:
    if(el== x):
        print("Using Break condition --- First expected number found at indix",idx)
        break
    idx +=1
    



# WAP to find the sum of first n numbers. (using while)
n = 7
sum = 0
i = 1
while i < n:
    sum += i
print ("total sum =", sum) 


for i in range(1, n+1):
    sum += i
print ("total sum =", sum)  




# WAP to find the factorial of first n numbers. (using for)
n = 3
fact = 1
i = 1
while i <= n:
    fact *= i
    i += 1
print ("factorial =", fact)


n = 5
fact = 1
for i in range (1, n+1):
    fact *= i
print("factorial =", fact)