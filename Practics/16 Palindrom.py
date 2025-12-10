numbeseries = [1,2,3,4,3,2,7]
print(numbeseries);
print(type(numbeseries))

copy_numbeseries = numbeseries.copy()
print(copy_numbeseries)

copy_numbeseries.reverse()
print(copy_numbeseries)

if(copy_numbeseries == numbeseries):
    print("Palindrom")
else:
    print("Not palidrom")

#----------------------------------------------------------------------------------------------------------------------------------

grade = ("a","f","y","f","r","f","a","p","a","A","A")
print(grade.count("a"))



Test_score = ["a","f","y","f","r","f","a","p","a","A","A"]
Test_score.sort()
print(Test_score)