#Python Basics2
"""Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""

#short version of if else statement
#if a > b: print("a is greater than b")
#or
a = 2
b = 330
print("A") if a > b else print("B")

#For Loop
colours = ["Red","Yellow","Blue","Black","White"]
for x in colours:
    print(x)
    if(x=="Yellow"):
        print("yellow yellow dirty fellow")



for x in range(1,10,2): #(start,end,spacing)
    print(x)
else:  # executed at the end of the loop
    print("finally finished!!")

#Nested For Loops

colour = ["Red","Yellow","Blue","Black","White"]
fruit = ["Apple","Banana","Mango","Cheery","Watermelon"]

for x in colour:
    for y in fruit:
        print(x,y)


#for loops cannot be empty, but if you for some reason have a for loop with no content, 
#put in the pass statement to avoid getting an error.

for x in [0, 1, 2]:
  pass



#While Loop
i=1
while i<=6:
    print(i)
    if i==3:
        break
    i=i+1    #also i+=1


i = 0
while i < 6:
  i += 1
  if i == 3:
    continue #skips this iteration and continues to the next iteration
  print(i)



i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("variable is no longer less than 6")

#Functions

def average(a,b=1):  #Considers 1 to be the default value for b
     c=((a+b)/2)
     print("Average is :",c)

average(1)

#Return Value

def average(*num):
  sum=0
  for i in num:
    sum=sum+i
  return sum

c=average(5,6,7,1)
print(c)

#List of Even and Odd

NumberList = [1,2,3,4,5,6,7,8,9,0]

for i in NumberList:
  if (i%2 == 0):
      print(i,"Number is Even!")
  else:
      print(i,"Number is Odd!")
print("Completed!")


for x in range(25):
    if (x == 1):
      continue
    if(x>5):
      break
    print(x)
   

Lon =[1,2,3,4,5,6,7,8,9,0]

for x in Lon:
    if(x%2==0):
      print(x,"is even")
    else:
      print(x,"is odd")


#Nested IfElse

height=int(input("Enter Your Height in cms"))

if height>=120:
  age=int(input("Enter Your Age :"))
  if age>=18:
    print(f"Since your height is {height} cms and age is {age} you can ride the rollercoaster ")
  else:
    print(f"Since your age is less than 18 you cannot ride the rollercoaster")
else:
   print("Your Height is Short for riding the rollercoaster")


#

total=0
#Sum of Numbers from 1to100
for num in range(1,101):
   total+=num

print(total)

#Sum of Even Numbers

target=int(input("Enter your desired target number"))

sum=0
for x in range (2,target+1,2):
   sum+=x
print(sum)

#Alternate Method
sum_1=0
for x in range (2,target+1):
  if(x%2==0):
      sum_1+=x
  else:  #else is not necessary
      pass
print(sum)


