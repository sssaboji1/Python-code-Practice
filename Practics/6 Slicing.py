#--------- slicing = accessing part of string

# str[tarting_idx : ending_idx]
# ending index is not icluded in slicing result


str = "This is the the kingdom of dreams"
print(str[1:9])
print(str[:9])
print(str[7:])

print(str[3:len(str)])
print(str[3:len(str)-3])


#------------ NEGATIVE INDEX ----------------
#Apple 

# +VE   -VE
# 0   A  -1
# 1   p  -2
# 2   p  -3
# 3   l  -4
# 4   e  -5

str = "Apple"
print("This is NEGATIVE Indexing : ->",str[-5:-1])



