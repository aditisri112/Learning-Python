age=input("enter your age") #by default it is of string type
print(type(age)) #output is str
print(int(age)) #converted to integer type manually -> type casting
new_age=int(age)+1
print(new_age)
print(type(int(age))) #output is int

print(1+2.5) #output is 3.5->interpreter by its own->type conversion
print(1+int(2.999)) #output is 3->manually->type casting