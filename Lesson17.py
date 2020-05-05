#Lesson 17

#Student Name:

"""
Today's lesson will be mostly work on anticipating the actions of a program. 
"""

teams = ["Warriors", "76ers", "Celtics", "Lakers", "Clippers"]

print("Problem 1")
for i in range(0, len(teams)):
  print(i)
  print(teams[i])

#Group:
"""
0 
Warriors
1 
76ers
2 
Celtics
3 Lakers
4 Clippers

0 
1 
2 
3 
4
Warriors 
76ers
"""
# -3 Celtics
# -2 Lakers
# -1 Clippers
# 0 Warriors
# 1 76ers

print("\nProblem 2")
for i in range(1, len(teams)+1):
  print(i)
  print(teams[-i])

"""
Group Guess:
1
Clippers
2
Lakers
3
Celtics
4
76ers
5
Warriors
"""

print("\nProblem 3")
for team in teams:
  print(team)
  if team == "Warriors" or team == "76ers":
    print("That's a home team")
  else:
    print("We don't root for that team")

"""
Seth Guess:
Warriors
That's a home team
76ers
That's a home team
Celtics
We don't root for that team
Lakers
We don't root for that team
Clippers
We don't root for that team
"""

fourByFour = [
  [1,2,3,4],
  [5,6,7,8],
  [9,10,11,12]
]
fourByFour.append([13,14,15,16])

print("\nProblem 4")

for innerList in fourByFour:
  print("A")
  for num in innerList:
    if num % 3 == 0:
      print("B")
print("C")

"""
Group Guess:
A
B
A
B
A
B
B
A
B
C
"""
#Keeton creates problem 4.5:
for i in range(5, 9):
  for j in range(-3, 8):
    print(i + j)

"""
Solution:
2
3
4
"""

#Seth creates problem 5:

#Andrew creates problem 6:

#Ryan creates problem 7:

print("\nProblem 8")
# def recur(num):
#   if num <= 0:
#     print("A")
#   else:
#     print("B")
#     return recur(num-1)

# recur(5)
# recur(-2)
# recur(0)
# recur(1)

#A helper function:
def printGrid(grid):
  for innerList in grid:
    print(innerList)

#Homework Problem
print("\nHomework Problem")

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

print("\nHint Homework")
#Hint for problem 1:
threeByThree[1][1] = 100
printGrid(threeByThree)