#Lesson 15

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

print("Homework Problem:")
"""
This function prints all (and only) elements on the diagonal of a grid
"""
def printDiags(grid):
  lenOfGrid = len(grid)
  for i in range(0,lenOfGrid):
    print(grid[i][i])
    # grid = grid + 1
    # print(grid)
    # # print(grid = grid + 1)
    # return(printDiags(grid))

def printDiags2(grid):
  lenOfGrid = len(grid)
  for rowNum in range(0, lenOfGrid):
    for colNum in range(0, lenOfGrid):
      if rowNum == colNum:
        print(grid[rowNum][colNum])

print("Hint: ")
# print(fourByFour[0][3])
# print(fourByFour[0][1])
print(fourByFour[0][0])
print(fourByFour[1][1])
print(fourByFour[2][2])
print(fourByFour[3][3])

print("Test Cases: ")
#Test for problem 2: 1 6 11 16
printGrid(fourByFour)
printDiags(fourByFour)
print()
#Another: NW SE
printGrid(directions)
printDiags(directions)

#Add your test cases here:
sethsList = [[0,1,7],[0,1,0],[6,1,0]]
printDiags(sethsList)     # 0 1 0

#Ryan's Test
abc = [[73,22],[89, 4]]
printDiags(abc)           #73 4

#Andrew's Test
andrewsList = [[1,5,3],[1,7,12],[19,20,14]]
printDiags(andrewsList)   #1 7 14

print("\nExample A")
def containsSingleList(myList, element):
  for thing in myList:
    if thing == element:
      return True

  return False

#Test 1: False
teams = ["Warriors", "Suns"]
print(containsSingleList(teams, "Lakers"))

#Add a test case here for example A
#Test 2: True
# element = "Harry Potter"
charactersInHP = ["Harry Potter", "Hagrid", "Voldemort", "Dobby"]
print(containsSingleList(charactersInHP, "Voldemort"))

#Add a third test case:
#Test 3: False
animals = ["Hippo", "Kangaroo"]
print(containsSingleList(animals, "Cow"))

print("\nProblem 1")
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

print("\nProblem 2")
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