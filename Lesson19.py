#Lesson 19

#Student Name:

#A helper function:
def printGrid(grid):
  for innerList in grid:
    print(innerList)

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

Classes allow us to create "objects". Objects are specific instances of their class.

-Data (fields)
-Methods (functions)
"""

print("\nIntro to Classes")
#We'll talk more about these next time but let's look at some examples.

class Rectangle():
  #constructor
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
    return self.width * self.height

print("Examples")
myRect = Rectangle(4,6)
print(myRect.isSquare())
myRect2 = Rectangle(5,5)
print(myRect2.isSquare())
myRect3 = Rectangle(9,6)
print(myRect3.isSquare())

#HW: Add a test case for myRect3.isSquare()

#Test cases for get area:
myRect4 = Rectangle(9,8)
print(myRect4.getArea())
myRect5 = Rectangle(3, 5)
print(myRect5.getArea())


# Example 2: Dating App

"""
Suppose we're Software Engineers and we're building a dating app for middle schools on the Main Line. People sign up for the app, and they fill out their profile with some information about themselves. Then they are shown a list of other users, and given an option to like them or not. If two users like each other, it's a match! They get to chat with each other online and decide if they want to meet in person. 
"""

#One class we'll definitely need for this app is a User class.

class User():
  def __init__(self, name, gender, age, genderPref, school):
    self.name = name
    self.gender = gender
    self.age = age
    self.genderPref = genderPref
    self.school = school
    self.interests = []
    self.bio = ""

  def getName(self):
    return self.name

  def getAge(self):
    return self.age

  def getSchool(self):
    return self.school

  def getInterests(self):
    return self.interests

  def setAge(self, inputAge):
    self.age = inputAge

  def setBio(self, inputBio):
    self.bio = inputBio

  def addInterest(self, inputInterest):
    #inputInterest is a string!
    self.interests.append(inputInterest)

print("\nExample 2: ")
user1 = User("Bob", "male", 12, "female", "Haverford")
print("Bob's age: ", user1.getAge())
user1.setAge(13)
print("Bob's age again: ", user1.getAge())

print("\nBob's interests: ", user1.getInterests())
user1.addInterest("Basketball")
user1.addInterest("Computer Science")
print("Bob's interests again: ", user1.getInterests())

#Example 3: Tic Tac Toe

class Game():
  def __init__(self):
    self.board = [
      [" ", " ", " "], 
      [" ", " ", " "], 
      [" ", " ", " "]
      ]

  def putX(self, row, col):
    self.board[row][col] = "X"

  def putO(self, row, col):
    pass

  def checkIfWinner(self, letter):
    #Letter is either X or O.
    pass

  def gameStatus(self):
    #Prints the board
    printGrid(self.board)

print("\nExample 3:")

#Make a game object for a test case here: 
game1 = Game()
game1.gameStatus()
print()
game1.putX(0,1)
game1.putO(1,1)
game1.gameStatus()


