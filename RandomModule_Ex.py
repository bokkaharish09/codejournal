#RandomModule
#Heads_Tails
import random

random_side = random.randint(0,1)
if random_side==1:
    print("Heads")
else:
    print("Tails")


#Banker Roulette

n_str=input("Enter the names of the people present :")
names=n_str.split(", ")
ln_name=len(names)

import random

random_side=random.randint(0,ln_name-1)

print(f"{names[random_side]} will pay the bill today")


