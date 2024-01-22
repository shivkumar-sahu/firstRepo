print("Welcome monu")
print("in Python World")
a=5
b=6
c=a*b
print("a*b =", c)
# a="{(clone)}"
print("clone")

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






