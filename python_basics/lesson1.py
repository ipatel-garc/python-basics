# variables are used store data values 
x= 5 # integer 
y=3.14 #float 
name= "Isabella" #string
# a letter is a list of characters in 
# quotation marks
is_student= True #boolean True or False
#print the values of the variables 
print(x)
print(y)
print(name)
print(is_student)
print("My name is " + name + ", I am " + str(x) + " years old.")
#the plus sigh (+) is used to concatenate strings
# str(x) converts the integer x into a string
# type() function returns the type of a variable
print(type(x)) # <class 'int'>
print(type(y)) # <class 'float'>
print(type(name)) # <class 'str'>
print(type(is_student)) # <class 'bool'>
# lets make a new set of variables to practice
a=10
b=2.5
c="Isabella"
d= False 
#Print the variables of the new variables in a sentence 
# using concatenation
print("My name is " + str(c) + ", I am " + str(a) + " years old.")
print(f"My name is {c}, I have {a} apples. I am {b} meters tall")
