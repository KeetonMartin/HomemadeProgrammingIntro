#Lesson 20
# Student Name: 

exampleTuple = ("me","you")

#Warmup: Classes
print("Warmup")
class Circle():
  def __init__(self, rad, center):
    self.radius = rad
    self.center = center    #This should be a tuple... What is that?

  def getArea(self):
    #3.14 times radius^2
    return 3.14 * (self.radius**2)

  def getRadius(self):
    return self.radius

#Put a line here that creates a circle object, centered at (2,4) with radius 3:
myCircle = Circle(3, (2,4))
myCircle2 = Circle(5, (-2,-3))
myCircle3 = Circle(5, (-2,-5))

#Put a line here that PRINTS the radius of the circle we made
print(myCircle2.getRadius())
#We expect 5

#Put a line here that PRINTS the area of the circle we made
print(myCircle.getArea())
print(myCircle2.getArea())
#We expect ~27


# Example from last time:
def printGrid(grid):
  for innerList in grid:
    print(innerList)

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
    self.board[row][col] = "O"

  def checkIfWinner(self, letter):
    #Letter is either X or O.
    #Check if winner returns true or false.
    board = self.board
    firstRow = board[0]
    secondRow = board[1]
    thirdRow = board[2]
    firstCol = [board[0][0], board[1][0], board[2][0]]
    secondCol = [board[0][1], board[1][1], board[2][1]]
    thirdCol = [board[0][2], board[1][2], board[2][2]]
    diag1 = [board[0][0], board[1][1], board[2][2]]
    diag2 = [board[0][2], board[1][1], board[2][0]]

    if firstRow == [letter, letter, letter] or secondRow == [letter, letter, letter]:
      return True
    elif thirdRow == [letter, letter, letter] or firstCol == [letter, letter, letter]:
      return True
    elif secondCol == [letter, letter, letter] or thirdCol == [letter, letter, letter]:
      return True
    elif diag1 == [letter, letter, letter] or diag2 == [letter, letter, letter]:
      return True
    else:
      return False

  def gameStatus(self):
    #Prints the board
    printGrid(self.board)
    print()

print("\nTic Tac Toe:")

#Make a game object for a test case here: 
game1 = Game()
game1.gameStatus()
game1.putX(0,1)
game1.putO(1,1)
game1.gameStatus()

game1.putO(1,2)
game1.putO(1,0)
game1.putX(0,0)
game1.putX(0,2)
game1.gameStatus()
#Now we should be able to check if O won
if game1.checkIfWinner("O"):
  print("O Wins!")

if game1.checkIfWinner("X"):
  print("X Wins!")

if game1.checkIfWinner("X") and game1.checkIfWinner("O"):
  print("Tie!")


#Game2 Test Case
print("\n Game 2:")
game2 = Game()

print("\n Game 3:")
game3 = Game()

#The next thing we'll do is create a match maker for our dating app

#I've copied over the code for our user class
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


class Matchmaker:
  def __init__ (self, users):
    self.users = users

  def checkInterestOverlap(self, user1, user2):
    #returns true if users share an interest, else returns false
    pass

  def matchMake(self):
    self.checkInterestOverlap(self.users[0], self.users[1])

#Create a user object:

#Create another:

#Create a matchmaker object with those 2 users as input:

#Call .matchMake()