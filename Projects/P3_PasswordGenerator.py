#Password Generator

#Input
char=int(input("How many letters do you need? \n"))
num=int(input("How many numbers do you need? \n "))
symb=int(input("How many symbols do you need? \n"))

#Database
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

password =""
import random


#Attempt1

# for char in range(1,char+1):
#     password += random.choice(letters)
# for num in range(1,num+1):
#     password += random.choice(numbers)
# for symb in range(1,symb+1):
#     password += random.choice(symbols)
# print(password)

#Attempt2
passwordlist=[]

for char in range(1,char+1):
    passwordlist.append(random.choice(letters)) 
for char in range(1,num+1):
    passwordlist.append(random.choice(numbers)) 
for char in range(1,symb+1):
    passwordlist.append(random.choice(symbols)) 
# print(passwordlist)

random.shuffle(passwordlist)

password = ""

for char in passwordlist:
    password +=char

print(password)






