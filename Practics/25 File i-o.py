# --------------------- File i/0 in Python (Input Output)--------------------

# Python can be used to perform operations on a file. (read & write data)


# ------------ Types of all files
# 1. Text Files: txt, docx, log etc.
# 2. Binary Files: mp4, mov, png, •jpeg etc.

# ------------ File Operations in Python
# 1. Create a file
# 2. Write data to a file
# 3. Read data from a file
# 4. Delete a file (Using OS module)  

f = open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/demo.txt","r") # inbuilt function to open a file
data = f.read()  # read() function to read the content of the file
print(data)
print(type(data))  # data type of the content read from the file
f.close()  # close() function to close the file after operations
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ 
f= open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/demo.txt","r")
line = f.readline()
print(line)  # readline() function to read a single line from the file

lineanother = f.readline()
print(lineanother)  # readline() function to read a single line from the file
f.close()
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ 

f = open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/demo.txt","w")
f.write("I got my Visa")  # write() function to write data to a file
f.close()
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------

f = open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/demo.txt","a")
f.write("\nI am travelling to Luxumburge ")  # append() function to add data to 
f.close()

# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------

f = open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/sampe.txt","w")
f.write("ABCD")

# ------------ ------------ ------------ ------------ ------------ ------------ ------------ -------
f = open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/sampe.txt","w+")
f.write("ABCD") #Result - ABCD and truncates the entier file
f.close()       

# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------   
f= open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/new_Test_file.txt","w")
f.write("Reach at Embassy for Visa Interview")
f.close()   
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------   
f= open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/new_Test_file.txt","r+")
f.write("XYZ")
f.close()   
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------   
f= open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/new_Test_file.txt","a+")
f.write("\nFinally all process done")
f.close()   
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------   
f= open("/Users/sushant.saboji/Downloads/Sush/Python/Python-code-Practice/Practics/new_Test_file.txt","w+")
f.write("This is your PR and visa approved")
f.close()  
# ------------ ------------ ------------ ------------ ------------ ------------ ------------ ------------ 


# ------------- Modes to open a file
# 'r' - Read mode - Default mode - Opens a file for reading only
# 'w' - Write mode - Opens a file for writing only
# 'a' - Append mode - Opens a file for appending data to the end of the file
# 'x' - Create mode - Creates a file, returns an error if the file exists
# 't' - Text mode - Default mode - Opens a file in text mode
# 'b' - Binary mode - Opens a file in binary mode   