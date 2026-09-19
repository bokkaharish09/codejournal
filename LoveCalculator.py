#Love Calculator

name1=str(input("What is your name?"))
name2=str(input("What is their name?"))
combine=str(name1+name2)

lc_name=combine.lower()

t=lc_name.count("t")
r=lc_name.count("r")
u=lc_name.count("u")
e=lc_name.count("e")

first_name=str(t+r+u+e)

l=lc_name.count("l")
o=lc_name.count("o")
v=lc_name.count("v")
e=lc_name.count("e")

second_name=str(l+o+v+e)

score=str(first_name+second_name)

print(f"Your score is {score}")

