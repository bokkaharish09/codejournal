
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


#Lambda Function
def Execute(f,x):
    return f(x)

print(Execute(lambda x:x*x*x,4))
    