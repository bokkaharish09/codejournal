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