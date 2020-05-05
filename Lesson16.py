#Lesson 16

#Student Name:

#These are from Lesson 13:
doubleList = [[1,2,3],[4,5,6]]
print(doubleList)

fourByFour = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
fourByFour.append([13,14,15,16])
print(fourByFour)

directions = [["NW", "NE"],["SW", "SE"]]
print(directions)

#A helper function:
def printGrid(grid):
  for innerList in grid:
    print(innerList)

#Now we have all our helpful things defined...

#Let's start with a warmup
print("Warmup time! Implement these functions")

print("Warmup 1:")
#Returns true if myList is empty, otherwise returns false
def isEmpty(myList):
  if myList == []: 
    return True
  else:
    return False

#Test 1: True
print(isEmpty([]))
#Test 2: False
print(isEmpty([1,2,3]))

print("\nWarmup 2:")
#Returns highest value integer in the list
def getHighestNum(myList):
  highestNum = -800
  for element in myList:
    print("A")
    if element > highestNum:
      print("C")
      highestNum = element
  print("B")
  return highestNum

#Ryan's Guess: AAAACB6
#Andrew's Guess: AAAAB
#Seth's Guess: ACBBCA

#Test 1: 6
print(getHighestNum([-2,0,6,3]))
#Test2: -3
# print(getHighestNum([-700, -4, -3]))
#Test 3:
# print(getHighestNum([5,6,7]))

#Let's review the homework
print("\nHomework Problem:")

"""
This function returns true if the element is in the grid, or returns false if it is not.
"""
def contains(grid, element):
  pass

#Test 1: True
print(contains(fourByFour, 8))
#Test 2: False
print(contains(fourByFour, 17))
#Test 3: True
print(contains(fourByFour, 7))
#Test 4: False
print(contains(directions, "N"))
#Test 5: 
#Test 6: 

#Problem 1:
print("\nProblem 1")
"""
This function takes a grid, and changes all numbers on the diagonal to be 1s. 
It then takes All numbers below the diagonal and changes them to be 2s.
It returns the changed array
"""
def modifyArray(grid):
  pass

#Test 1:
threeByThree = [[1,2,3],[4,5,6],[7,8,9]]
printGrid(threeByThree)
print(modifyArray(threeByThree))
#Should give us: [[1,2,3],[2,1,6],[2,2,1]]
print("above should match this:")
printGrid([[1,2,3],[2,1,6],[2,2,1]])

#Test 2:

#Test 3:

print("\nHint Problem 1")
#Hint for problem 1:
threeByThree[1][1] = 100
printGrid(threeByThree)