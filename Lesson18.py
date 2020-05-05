#Lesson 18

#Student Name:

#Helpers:
#A helper function:
def printGrid(grid):
  for innerList in grid:
    print(innerList)

teams = ["Warriors", "76ers", "Celtics", "Lakers", "Clippers"]

fourByFour = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
fourByFour.append([13,14,15,16])
threeByThree = [[1,2,3],[4,5,6],[7,8,9]]

#Let's start by going over the homework! (Problem 5,6,7)

print("Problem 5")
harryPotter = ["i", "j"]
jellyBeans = ["j", "i"]

for letter in jellyBeans:
  if harryPotter == ["i", "j"]:
    jellyBeans = ["j", "i"]
    print("guitar")

print("Problem 6")
nums = [9, 12, 10]
for num in nums:
  if num % 3 == 0:
    print("Potato")

100 % 3
21 % 4
36 % 4
"""
print("Problem 7")
EvenTests = [2,77,44,52,99,73]
for EvenTest in EvenTests:
  if EvenTest % 2 == 0:
    print(EvenTest)
  else:
    print("False")
for EvenTest in EvenTests:
  for i in range(0, len(EvenTests)):
    print("R")
"""
#Problem 1: Recursion Review

print("\nProblem 1")
def recur(num):
  if num <= 0:
    print("A")
    return
  else:
    print("B")
    return recur(num-1)

#BBBBA
recur(5)

#A
recur(-2)

#A
recur(0)

#BA
#BAAAAAAAAAAAA
#1
recur(1)

#Now for some new content:
"""
Classes in python!

Classes allow us to define our own variable TYPES. We already know about a few variable types. In computer science in general, primitive data types are:

-Booleans
-Ints
-Characters

We've now also seen more complex data types:

-Strings
-Lists
-Lists of Lists
-(Dictionaries)
-(Trees)
-(Stacks)

But what if we want our own datatype instead of a built in one?

Classes allow us to create "objects". Objects are made up of

-Data (fields)
-Methods (functions)
"""

print("\nIntro to Classes")
#We'll talk more about these next time but let's look at some examples.

class Rectangle():
  def __init__(self, height, width):
    self.width = width
    self.height = height

  def isSquare(self):
    #Should return true or false
    if self.width == self.height:
      return True
    else:
      return False

  def getArea(self):
    #Implement here
    pass

print("Examples")
myRect = Rectangle(4,6)
print(myRect.isSquare())
myRect2 = Rectangle(5,5)
print(myRect2.isSquare())

#HW: Add a test case for myRect3.isSquare()

#Test cases for get area: