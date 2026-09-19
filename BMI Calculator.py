#1st Input Height
h=float(input("Enter your Height in (meters)="))
#2nd Input Weight
w=int(input("Enter your Weight in (kilograms)="))
#Calculation for BMI
# print("Your Calculated BMI is",(w/(h*h)))
bmi=w/(h**2)
# F-String
print(f"Your BMI for when height is {h} and Weight is {w} comes out to be {round(bmi,2)}")
# bmi=w/(h*h)
# print("Your Calculated BMI is",bmi)






