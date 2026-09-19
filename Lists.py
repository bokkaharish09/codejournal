
"""
append()	Adds an element at the end of the list
clear()	Removes all the elements from the list
copy()	Returns a copy of the list
count()	Returns the number of elements with the specified value
extend()	Add the elements of a list (or any iterable), to the end of the current list
index()	Returns the index of the first element with the specified value
insert()	Adds an element at the specified position
pop()	Removes the element at the specified position
remove()	Removes the item with the specified value
reverse()	Reverses the order of the list
sort()	Sorts the list"""


#Lists[]
#Tuples() Cannot be changed after definition

x=[1,2,3,4,5,6]

[print(i) for i in x]  # short hand version of for loop

for i in range(len(x)):
    print(i,":",x[i])

i=0
while i<len(x):
    print(i,":",x[i])
    i+=1


#print(x[:3])#First 3 Elements
#print(x[3:])#Last 3 Elements
print(x[-1])#Negative Indexing starts from the end

x.extend([7,8])
print(x)

x.insert(1,"One")
print(x)

x.append(9)
print(x)

#syntax to remove list items
"""x.remove("One")
x.pop(1)
del x(1)
x.clear()"""


y=[6,7,8,9]
lol=[x,y] #listoflist

x.extend(y)
print(x)

print(lol)
print(y[1])

#Splitting Strings

(age,income)="25,120000".split(',')
print(age)
print(income)

[age,income]="25,120000".split(',')
print(age)
print(income)


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []

for x in fruits:
  if "a" in x:
    newlist.append(x)

print(newlist)

#List Sorting

x=[24,26,19,89,46,13,0,2]
"""
x.sort()
print(x)

x.sort(reverse=True)
print(x)
"""

def average(x):
   return sum(x)/len(x)

avg=average(x)
#print(avg)

def absfunct(n):
   return abs(n-avg)

x.sort(key=absfunct)
print(x)


fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[0][3])