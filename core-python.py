import myModule as myM
from myModule import person1 as pr
import datetime
import json
import os


if 5 > 2:
    print("Five is greater than two!")


#Variables
x = 10
y = "Hello"

print(x)
print(y)
#print(x+y)


"""
this is a multi line comment 
xxxxxxxxxxxxxxxxxxxxxxxxxxxxx
"""

a, b, c = 10, 1, 5

a = b= c = 9
print(a)
print(b)
print(c)

print(type(c))

firstName = "Michael"
print("Welcome Mr."+firstName)


#Mathemetical Ops

num1 = 10
num2 = 20

sum = (num1 + num2)

print(sum)


name = "Blah"

def muFunc():
    global name
    name = "foo"
    print("There is some "+name)

muFunc()

print(name)


age = 30
dob = 26051989

text = "I am {} born so my age is  {}"

txtDynamic = text.format(dob, age)
print(txtDynamic)


## Boolean checks

print( 10 > 5)
print (12 < 5)

print( 1 == 1)

print(bool("hello"))
print(bool(5))

print(bool(""))
print(bool(0))
print(bool(None))


print(11/3)
print(11%3)
print(11**3)


###List - Ordered, changeble, indexed, allows duplicate
cars = ["bmw", "audi", "kia"]

cars[2] = "benz"
for car in cars:
    print(car)  

if "benz" in cars:
    print("Yoooo! Benz is there bro")

print(len(cars))

cars.append("Skoda")
print(cars)

cars.insert(1, "Maruthi")
print(cars)

cars.remove("Maruthi")
print(cars)


cars.pop()
print(cars)

cars.append("benz")
print(cars)

del cars[3]
print(cars)

#cars.clear()
print(cars)

newCars = cars.copy()
print(newCars)

allCars = cars + newCars
print(allCars)

for car in newCars:
    cars.append(car)
print(cars)

cars.sort()
print(cars)

cars.sort(reverse=True)
print(cars)


### Tuples - Ordered, unchangeble, idexed, allows duplicates

bikes = ("TVS", "Suzuki", "Bajaj")
print(bikes)

print(len(bikes))

print(bikes[1])

bikeLists = list(bikes)

bikeLists[1] = "Honda"

print(bikeLists)


for bike in bikes: 
    print(bike)

if "Honda" in bikes:
    print("Yes, Honda is available in above tuple")
print("No, Honda is not available in above tuple")


print(type(bikes))
print(type(bikeLists))



### Sets - unordered, unindexed and No duplicate values

colors = {"red", "green", "blue"}

print(colors)

for color in colors:
    print(color)

print("red" in colors)

colors.add("Orange")
print(colors)

colors.update(["black", "white", "Grey"])
print(colors)

print(len(colors))

colors.discard("pink")
colors.remove("Grey")
print(colors)



### Dictonaries  - unordeded, indexed, changeble and No duplicate values

myCar = {
    "Brand": "Maruthi",
    "Color":"white",
    "kms": 20000
}

print(myCar)
print(myCar["kms"])
print(myCar.get("kms"))

myCar["kms"] = 21000
print(myCar.get("kms")) 

for prop in myCar:
    print(prop)


for prop in myCar:
    print(myCar[prop])

for prop in myCar.values():
    print(prop)

for x, y in myCar.items():
    print(x, y)

if "modal" in myCar:
    print("True")
print("False")

print(len(myCar))

myCar["Modal"] = "Swift"
print(myCar)

print(myCar.keys())


### If else block
myInt = 10
myInt2 = 20

if myInt > myInt2:
    print("1st one is bigger number")
elif myInt == myInt2:
    print("Both are same numbers")
else:
    print("2nd number is bigger than 1st number")

### Shorthand property for if else
if myInt < myInt2: print("1st number is less than 2nd number") 

if myInt < myInt2 or myInt != myInt2: print("1st number is less than 2nd number ||  atleast they are not equal")


def greet(who = "world"):
    print("Hello, "+ who)

greet("Pk")
greet()

def getCars():
    for car in cars:
        print(car)

getCars()

def getTasks(tasks):
    for task in tasks:
        print(task)

getTasks(["Get up", "Fresh up", "Get Ready", "Eat", "Travel to work", "Work in office", "Do Gym", "Go home", "Fresh up", "Enjoy", "Sleep"])


def multiply(x):
    return x*5

result = multiply(5)
print(result)



#Lambda function
x = lambda a: a + 10
print(x(5))

y = lambda a, b: a+b
print(y(5, 4))


def myLfunc(n):
    return lambda a: a *n

myDoubler = myLfunc(2)

result = myDoubler(3)

print(result)


# Classes in Python
class MyClass:
    x = 5

print(MyClass)

p1 = MyClass()
print(p1.x)


#__init__() function for class

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myDetails(self):
        print("My Name is "+self.name)

p1 = Person("Scott", 16)
p2 = Person("Will", 10)

print(p1.name, p1.age)
print(p2.name, p2.age)
p1.myDetails()
p2.myDetails()


#Inheritance in python

class Student(Person):
    pass # If no properties are required to be added then just add pass statement

s1 = Student("Mike", 11)

s1.myDetails()

class Child(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.gender = "M"

    def greet(self):
        print("Welcome Mr/Ms."+self.name, self.gender)

c1 = Child("Chris", 65)
c1.greet()


#Iterator vs Iterable

myTuple = ("Pencil", "Pen", "Sharpner", "Box")

myIt = iter(myTuple)

print(next(myIt))
print(next(myIt))
print(next(myIt))
print(next(myIt))

#This can be used by for loop which internally does the iteration
for temp in myTuple:
    print("for--"+temp)


# Iterating the strings
myString = "Iamhappybro"

myStr = iter(myString)

print(next(myStr))
print(next(myStr))
print(next(myStr))
print(next(myStr))
print(next(myStr))
print(next(myStr))

#Strings also can be iterated by using the for loop
for temp in myString:
    print("for --"+ temp)

# Importing the modules and using it
myM.greet()


#Built in modules
import platform
x = platform.system()
print(x)

# y = dir(platform)
# print(y)


print(pr['name'])

#Python dates

now = datetime.datetime.now()
print(now)
print(now.year)
print(now.strftime("%A"))

#Creating date object

dateObj = datetime.datetime(2020, 1, 19)
print(dateObj)

print(dateObj.strftime("%B"))


#Working with json

xJson =  '{ "name":"John", "age":30, "city":"New York"}'

yParsed = json.loads(xJson)

print(yParsed["age"])


# a Python object (dict):
xPythondDict = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

yJson = json.dumps(xPythondDict)
print(yJson)

#Exception Handling

try:
    print(x1)
except:
    print('An Excelption occuered')


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")

# Command line arguments
print("Enter your machine name")
#laptop = input()
#print("You may be using a machine which is a ", laptop+ " laptop")


#File Reading
file = open("C:\\Users\\pperiyas\\Desktop\\test.txt")
# To Read all data in the file
print(file.read())

#To Read only few charectors in the file
print(file.read(3))

#To read line by line
print(file.readline())
print(file.readline())
print(file.readline())

#To Iterate the files line by line

for line in file:
    print(line)

file.close()

# To append/write on the file
f = open("C:\\Users\\pperiyas\\Desktop\\test.txt", "a")
f.write("This is a new content inside the file")
f.close()

f = open("C:\\Users\\pperiyas\\Desktop\\test.txt", "r")
print(f.read())

#To write or override the file

f = open("C:\\Users\\pperiyas\\Desktop\\test.txt", "w")
f.write("Woops!, I've deleted the content")
f.close()

f = open("C:\\Users\\pperiyas\\Desktop\\test.txt", "r")
print(f.read())


#Create a new file 
f = open("C:\\Users\\pperiyas\\Desktop\\newtxtfile.txt", "w")
f.write("Hey wassup!")
f.close()

#Delete the files
"""if os.path.exists("C:\\Users\\pperiyas\\Desktop\\newtxtfile.txt"):
  os.remove("C:\\Users\\pperiyas\\Desktop\\newtxtfile.txt")
else:
  print("The file does not exist")


#Remove folder
if os.path.exists("C:\\Users\\pperiyas\\Desktop\\dummy"):
    os.rmdir("C:\\Users\\pperiyas\\Desktop\\dummy")
else:
    print("The folder does not exist")  """



myM.greet()


