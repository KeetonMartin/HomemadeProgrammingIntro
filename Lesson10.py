#Lesson Number 10

#With Ryan, Seth, and Andrew

#We'll start by going over the homework.

"""Here is Fib from lesson 9"""
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

print("\n", fib(4), "\n")

"""Now here is the blank fac function"""
def fac(n):
  #First and only base case:
  if n == 1:
    return 1
  #Recursive case:
  else:
    return n * fac(n-1)

for n in range(1, 8):
  print(fib(n))

print()

for n in range(1, 10):
  print(n)
  print(fac(n))

"""
Section 2: Recursion with lists
"""

#Let's define some lists. Fill these in with some elements
list1 = ["NBA", "NFL", "MLB"]
list2 = [4, 5, 6, 7]

for element in list1:
  print(element)

#let's fill in these functions

#this should return the first element of a list
def head(myList):
  return myList[0]

print(list1)
print(head(list1))

#this should return a list of all elements except the first
def tail(myList):
  return myList[1:]

print(tail(list2))
print("Guess what happens next!")
print(list1)
print(head(tail(list1)))
print(list2)
print(head(tail(list2)))

"""
Building our own recursive functions
"""

#Below this line, build a recursive function that prints all even numbers less than input n

def printEvens(n):
  pass