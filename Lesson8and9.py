#Lesson 8, Recursion, taught also during day 9
#First Name: 

"""
Some List practice to warm up!
"""

#Create an empty list:
KeetonList = []
#Append exactly 4 elements to your empty list:
KeetonList.append("Apple")
KeetonList.append("Orange")
KeetonList.append("Pear")
KeetonList.append("Strawberry")
#Print your list so far:
print(KeetonList)
#Print the 1st element:
print(KeetonList[0])
#Print the 3rd element (trick question!):
print(KeetonList[2])
#

#Moving into recursion

#Problem 1: recursion
print("Example 1:")
"""
Example 1 of Recursion:

Every recursive function has at least one base case.
It also has at least one recursive case.

Lets see an example. Fibonacci numbers.
https://en.wikipedia.org/wiki/Fibonacci_number
"""
def fib(n):
  #first base case
  if n == 0:
    return 0
  #second base case
  elif n == 1:
    return 1
  #recursive case
  else:
    return fib(n-1) + fib(n-2)

for n in range(0, 8):
  print(fib(n))

print(fib(2))

print("\nTry it yourself: ")
"""
Now time to try recursion yourself:

factorials!
https://en.wikipedia.org/wiki/Factorial
"""

def fac(n):
  #First (and only?) base case:
  if n == 1:
    return 1
  #Recursive case:
  else:
    return _________

  
print(fac(1))
print(fac(2))

#Problem 2 (for next time?):
"""
Recursion with lists
"""
def head(myList):
  pass

def tail(myList):
  pass