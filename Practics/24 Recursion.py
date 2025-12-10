# ------------------------- Recursion --------------------
# When a function calls itself repeatedly.
# prints n to 1 backwards 

def show(n):
    print(n)

# ---------------------------------------------------------------------------
# RECURSIVE Function

def show(n) :
    if (n == 0): 
        return   # when we rae rentun a nothing means it is CONTROL RETURN, there is no any as a such value
    print (n)
    show (n-1)

show(5)


def show(n) :
    if (n == 0): 
        return   
    print (n)
    show (n-1)
    print("END") # This END print end after retun value -- Call stack process  -- time 42:00 --https://www.youtube.com/watch?v=OvTH-7ESoRA&list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&index=6

show(10)

# ---------------------------------------------------------------------------
def fact(n):   # 52:00 time video for explantion https://www.youtube.com/watch?v=OvTH-7ESoRA&list=PLGjplNEQ1it8-0CmoljS5yeV-GlKSUEt0&index=6
    if(n == 1 or n ==0 ):
        return 1
    return fact(n-1) * n

print("Factorial is", fact(5))



# ---------------------------------------------------------------------------
# Q1. Write a recursive function to calculate the sum of first n natural numbers.






# ---------------------------------------------------------------------------
# Q2. Write a recursive function to print all elements in a list.
# Hint: use list & index as parameters.

