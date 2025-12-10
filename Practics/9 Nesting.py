#--------------NESTING---------------

physics_marks = int(input("Enter your physic marks :"))
maths_marks = int(input("Enter your maths marks :"))
chemistry_marks = int(input("Enter your chemistry marks :"))
total_marks = int(input("Enter your total marks :"))

if (physics_marks>=75 and maths_marks>=75 and chemistry_marks>=75):
    if(total_marks <= 75):
        print("you are not qualified for proceed further")
    else:
        print("your group is qualified")
else:
    print("denied")
