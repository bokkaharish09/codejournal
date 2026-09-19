
#Python Basics1
#1st Python Code File
#cmd+shift+p to select interpretor
#cmd+/ to comment

#Virtual Env
#-m venv *name
#source *name/bin.activate


#basic print statements
print("Hello World",7)
print(16*23)
print("EndCode")
print("_ "*10)

print("Hello "+input("What is your name?"))

#datatypes
a = "Harish_Bokka"
print(a)
print("Type of A is",type(a))

#everything in python is an Object

#input output code
"""
MultiLine Comments can be made using triple quotes
"""

#Casting
x=str(3)
y=int(3)
z=float(3)

print(x,y,z)


#for strings both single quotes and double quotes work
x='Harish'
y="Harish"
print(x,y)

#All variable names are case sensitive
"""
List [] mutable
Tuple () cannot be changed
"""

#Strings
a="Harish_Bokka_"
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("_")) #only strips characters from the end
print(a[0:5])
print(a.replace("Harish","Harry"))
print(a.split("_"))


#F-Strings
a="python for data analysis"
txt=f"I am learning {a}"
print(txt)
#More techniques in string formatting on W3school
