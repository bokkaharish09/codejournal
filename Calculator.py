#Calculator using Python
'''print("******CALCULATOR******")

print("Insert First Number")
input_a=float(input())



print("Insert Second Number")
input_b=float(input())

print("What Operation would you like to perform?")
print(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Dvision \n 5. Floor Division \n 6. Modulus \n 7. Exponential")

input_c=float(input())

if input_c == 1:
    print(input_a+input_b)
elif input_c == 2:
    print(input_a-input_b)
elif input_c == 3:
    print(input_a*input_b)
elif input_c == 4:
    print(input_a/input_b)
elif input_c == 5:
    print(input_a//input_b)
elif input_c == 6:
    print(input_a%input_b)
elif input_c == 7:
    print(input_a**input_b)
else:
    print("Invalid Input")'''

#Optimised Version

input_a=float(input("Insert First Number"))
input_b=float(input("Insert Second Number"))

print("What Operation would you like to perform? \n")

input_c=float(input(" 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Dvision \n 5. Floor Division \n 6. Modulus \n 7. Exponential \n"))

if input_c == 1:
    print(input_a+input_b)
elif input_c == 2:
    print(input_a-input_b)
elif input_c == 3:
    print(input_a*input_b)
elif input_c == 4:
    print(input_a/input_b)
elif input_c == 5:
    print(input_a//input_b)
elif input_c == 6:
    print(input_a%input_b)
elif input_c == 7:
    print(input_a**input_b)
else:
    print("Invalid Input")


#Tip Calculator
print("|| Welcome to Tip Calculator ||\n")

bill_amount=float(input("What is your total bill amount?"))

temp_var=input(print("Would you like to tip?(Yes/No)"))


def calculate_bill(x,y):
    if(y=="Yes"):
        tip=float(input(print("How much %Tip would you like to give?")))
        tip=tip/100
        x= x+(x*tip) 
        return x
    else:
        return x
    

bill_amount=calculate_bill(bill_amount,temp_var)

n=int(input(print("How many people are splitting the bill?")))

if(n==0):
    print("You should pay",round(bill_amount,2))
else:
    print("Each Person Should Pay :",round(bill_amount/n,2))