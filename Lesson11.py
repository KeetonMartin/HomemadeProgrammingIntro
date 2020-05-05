#Lesson 11, with Keeton

"""
Building our own recursive functions
"""

print("Modulo function, also known as mod")
print(10 % 3)
print(15 % 5)
print(20 % 17)
print(5 % 2)
print(14 % 2)
print(15 % 2)

print("\nProblem 1: ")

#this should return the first element of a list
def head(myList):
  return myList[0]

#this should return a list of all elements except the first
def tail(myList):
  return myList[1:]

def loopPrintEvens(myList):
  for element in myList:
    if element % 2 == 0:
      print(element)

#Below this line, build a recursive function that prints all even numbers in the list
def recursivePrintEvens(myList):
  if myList == []:
    return
  elif head(myList) % 2 == 0:
    print(head(myList))
  else:
    recursivePrintEvens(tail(myList)))

print("Loop example: ")
loopPrintEvens([1, 2, 3, 4, 5, 6])

print("\nRecursive example: ")
recursivePrintEvens([1, 2, 3, 4, 5, 6])


print("\nProblem 2: ")

#This is a loop-based way to print all elements
def loopPrintAllElements(myList):
  for element in myList:
    print(element)

#Build a recursive function that prints all elements of the input list
def printAllElements(myList):
  pass

#If there's time, implementing a recursive search() function