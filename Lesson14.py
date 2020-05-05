#Lesson 14

#More lists of lists

#These are from last time:
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

#We'll start by going over the homework

print("\nProblem 1:")
"""
This function should return the sum of the numbers in the grid
"""
def sumOfGrid(doubleList):
  #We only refer to doubleList
  sumSoFar = 0
  #One for loop here
  for innerList in doubleList:
    #Another for loop here
    for element in innerList:
      sumSoFar += element

  return sumSoFar

def sumOfGrid2(doubleList):
  for innerList in doubleList:
    for element in innerList:
      return sum(innerList)

#Here's a test
print(sumOfGrid(fourByFour))
#What should that print? Does it work when function is implemented?

#Here's Another
print(sumOfGrid(doubleList))
print("Bonus: ")
print(sumOfGrid2(doubleList))

#Andrew's Test Case: 
print(sumOfGrid([[2,4,7,12],[19,24,9]]))

#Ryan's Test Cases:
extraList1 = [[1,2],[3,4,5]]
print(sumOfGrid(extraList1))
extraList2 = [[2,4],[6,8,10]]
print(sumOfGrid(extraList2))

#Seth Test Case:
sethsFibs = [[1,2,3,5,8,13,21],[1,3,8,21]]
print(sum([1,2,3,5,8,13,21,1,3,8,21]))
print(sumOfGrid(sethsFibs))

def printGrid(grid):
  for innerList in grid:
    print(innerList)

print("\nProblem 2: ")
"""
This function prints all (and only) elements on the diagonal of a grid
"""
def printDiags(grid):
  lenOfGrid = len(grid)
  for i in range(0,lenOfGrid):
    print()

print("Hint: ")
# print(fourByFour[0][3])
# print(fourByFour[0][1])
print(fourByFour[0][0])
print(fourByFour[1][1])
print(fourByFour[2][2])
print(fourByFour[3][3])

#Test for problem 2: 1 6 11 16
printGrid(fourByFour)
printDiags(fourByFour)
print()
#Another: NW SE
printGrid(directions)
printDiags(directions)

#Add your test cases here:
sethsList = [[0,1,7],[0,1,0],[6,1,0]]
printDiags(sethsList)

print("\nExample A")
def containsSingleList(myList, element):
  for thing in myList:
    if thing == element:
      return True

  return False

#Test 1: False
teams = ["Warriors", "Suns"]
print(containsSingleList(teams, "Lakers"))

print("\nProblem 2")
"""This contains version checks through a whole grid for the element and returns T/F"""
def contains(grid, element):
  pass

#Test 1: True
print(contains(fourByFour, 8))
#Test 2: False
print(contains(fourByFour, 17))



print("\nProblem 3")
"""
This function takes a grid, and changes all numbers on the diagonal to be 1s. 
It then takes All numbers below the diagonal and changes them to be 2s.
It returns the changed array
"""
def modifyArray(grid):
  pass

#Test 1:
threeByThree = [[1,2,3],[4,5,6],[7,8,9]]
print(modifyArray(threeByThree))