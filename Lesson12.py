#Lesson 12

def head(myList):
  return myList[0]

def tail(myList):
  return myList[1:]

print("\nProblem 1: ")

#This is a loop-based way to print all elements
def loopPrintAllElements(myList):
  for element in myList:
    print(element)

#Build a recursive function that prints all elements of the input list
def printAllElements(myList):
  if myList == []:
    return
  else:
    print(head(myList))
    printAllElements(tail(myList))

#Test case 1A
print("\nTest1A:")
printAllElements(["Apple", "Banana", "Pear", "Peach"])
#Test case 1B
print("\nTest1B:")
loopPrintAllElements(["Apple", "Banana", "Pear", "Peach"])
#Test case 2A
print("\nTest2A:")
printAllElements(["Snow", "Rain"])
#Test case 2B
print("\nTest2B:")
loopPrintAllElements(["Snow", "Rain"])
#Add your test case below,
#Test Case 3A:
print("\nTest3A:")
printAllElements([6, 7, 8])



print("\nProblem 2:")
#If there's time, implementing a recursive search() function

#This function returns true if myList contains element or returns false if not. Use a recursive approach.
def contains(myList, element):
  #If empty
  if myList == []:
    return False
  #Elif head satisfies condition
  elif head(myList) == element:
    return True
  #Else recurse on tail
  else:
    return contains(tail(myList), element)

#Test case 1 - False
print(contains(["Fall", "Winter"], "Spring"))

#Test case 2 - True
teams = ["warriors", "lakers", "celtics"]
print(contains(teams, "lakers"))

#Test case 3 - True
games = ["fortnite", "minecraft", "roblox"]
print(contains(games, "minecraft"))

#Test case 4 - False
print(contains(games, "league of legends"))

#Test case 5
#Test case 6