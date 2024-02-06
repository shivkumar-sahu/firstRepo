

a=5
b=6
c=a*b
print("a*b =", c)
# a="{(clone)}"
print("clone")

a=int(input("Enter here first name:"))
print(a)

a=33
b=4
sum=a+b
print("the sum of given two number is",sum)
num1=float(input("enter first nuber here:"))
num2=float(input("enter another number here:"))
sum=num1+num2
print("add two number sum:",sum)

#convert a dictionary into a list of tuples.
a_dictionary={'a':1,'b':2,'c':3}

a_view=a_dictionary.items()
a_list=list(a_view)
print(a_list)

#age defined
old_age=input("enter your old age":)
new_age=int(old_age)+3
print(new_age)

a=input("enter yoiur first name:")
b=input("enter your alst name:")
d=input("contact no:")

c= a+b+d
print("your name:",c)

#square root no.
import math
num=int(input("Enyter a number here:"))
sr=math.sqrt(num)
print("The square root of the given number is:",sr)

#height and base area defined
height=(input("enter the heigh of the tringle"))
base=(input("enter the base of the tringle"))
area=(1\2)*base*height
print("The area of the tringle is",area)
#without using 3rd variable
x=25
y=52
x,y=y,x
print("the value of x is",x)
print("the value of y is",y)

#convert kilometer to miles
km=float(input("Enter your value in km:"))
miles=(0.621371)*km
print(km,"kms in miles will be",miles,"miles")

#check a number positive,negative and zero.
num=int(input("Enter a number here:"))
if num>0:
  print("it is a positive number")
elif num==0:
  print("it is zero")
else:
  print("it is a negative number")

#even and odd number
a=(input("Input number here:"))
if a %2==0:
print("it is an even number:")
else:
print("it is an odd number:")

# leap year find 
year=int(input("Enter a year:"))
  if()year%400==0)and(year%100==0):
    print(year,"is a leap year")
elip(year%4==0)and (year%100!=0):
   print(year,"is a lep year:")
else:
  print(year,"is not leap year")

# find the largest  among three numbers.
num1=12
num2=34
num3=99
if (num1>num2)and(num1>num3):
  print(num1,"is the largst number")
elif(num2>num3)and(num2>num3):  
  print(num2,"is the largest number")
else:
  print(num3,"is the largest number")
  #check prime number
num=int(input("enter number here:"))
if num==1:
  print("it is not a prime number")
if num>1:
  for i in range (2,num):
    if num % ==0:
      print("it is a prime number")
else:
  print("it is a prime number")
  #generate a random number

import random
num=random.randint(0,10)
print(num)

#print all prime numbers
lower=int(input("enter lower limit here:"))
upper=int(input("enter upper limit here:"))
for num in range (lower,upper+1):
  if num>1:
    for i in range (2,num):
      if num%i==0:
        break
      else:
        print(num)

#print assending order to dissending order

my_str = "python"
x =0

for i in my_str:
    x+=1
    print(my_str[0:x])

for i in my_str:
    x-=1
    print(my_str[0:x])  

#convert celsius to fahrenheit
celsius=int(input("enter tempreture in celsius:"))
fehrenheit=(celsius*(1.8))+32
print("The cinverted value is",fahrenheit,"fahrenheit")

a=int(input(enter no.here:))
print(a)

#user inpit
a=float(input("first number here:"))
b=float(input("second number here:"))

c=a+b
print(c)

def greet(name):
  print("hello",name)
 #pass arguments
  greet("sahoo")
   #two number add pre defined 

num1=40
num2= 34

print("the sum of the given two number is :",num1+num2)


x=int(input("enter the valu o x:"))
match x:
    case 0:
        print("x is zero")
    case 4:
        print("case is 4")
        case_:
        print(x)

 #using recursion  factorial no.
def fact(a):
  if a==0:
    return 1
  else:
    return((a)*fact(a-1))
    num=int(input("enter a number here:"))
    result=fact(num)
print("the factorial of the given number is ",result)

#table ko print karna

n=int(input("enter number here:"))
for i in range(1,11):
  print(n,"x",i,"=",n*i)





