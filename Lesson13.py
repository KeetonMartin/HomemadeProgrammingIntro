# Lesson 13

# Author: Keeton Martin
# Student Name: 

#Lists of Lists
"""
We've seen how lists can contains different types of variables. They can look like

[1,2,7,9]
or
["sent", "a", "letter", "around", "world"]
or even
[True, True, False]

We've also seen that strings are just lists of characters.
"""
print(list("Look! This was a string"))

"""
But, we know that lists are variables too (in a way)

So, believe it or not, we can make lists of lists!
"""

doubleList = [[1,2,3],[4,5,6]]
print(doubleList)

# pretty cool huh?

#What about normal list operations?
print("Example A")
print(doubleList[0])
print(doubleList[1])

print("Example B")
print(doubleList[0][0])
print(doubleList[0][1])

print("Example C")
for element in doubleList:
  print(type(element))
  print(element)

print("Example D")
for innerList in doubleList:
  # print("A")
  for element in innerList:
    # print("B")
    print(element)

#Ryans Guess: ABBBABBB
#Seth/Andrew Guess: AB1B2B3AB4B5B6

print("Example E")
fourByFour = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]

#Oops! That's only 3x4. Let's use append to fix it

fourByFour.append([13,14,15,16])

print(fourByFour)

"""
Now let's print this matrix. Note: lists of lists can be called
- matrices
- 2D Arrays
- "grids"
- "lists of lists"
"""

print("Example F")
for row in fourByFour:
  print(row)

print("Example G")
directions = [["NW", "NE"],["SW", "SE"]]
for row in directions:
  print(row)

print("Problem 1:")
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


#Here's a test
print(sumOfGrid(fourByFour))
#What should that print? Does it work when function is implemented?

#Here's Another
print(sumOfGrid(doubleList))

print("Problem 2")
"""
This function prints all (and only) elements on the diagonal of a grid
"""
def printDiags(grid):
  pass

#Test for problem 2
printDiags(fourByFour)
#Another
printDiags(directions)