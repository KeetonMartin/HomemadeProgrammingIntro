#Lesson 7 topics

#Problem 1
"""
Write a function taking in a string like "WOW this is REALLY amazing" and returning "Wow this is really amazing". String should be capitalized and properly spaced.

Hint: Try using functions like 
"APPLE".lower()
or
ourList = "Multiple words in a string".split()
["Multiple", "words", "in", "a", "string"]
"""
def filter_words(st):
  #We know st is a sentence
  temp = st.split()
  print(temp)

  returnable = []
  for word in temp:
    returnable.append(word.lower())

  return returnable
    
print(filter_words("Big Burritos WAKE UP"))

print("ExAMple".lower())
print("ExAM PLE").split()

#Lesson 8 topics
"""
You need to write a function that reverses the words in a given string. A word can also fit an empty string. If this is not clear enough, here are some examples:

backwards('Hello World') == 'World Hello'
backwards('Hi There.') == 'There. Hi'

As the input may have trailing spaces, you will also need to ignore unneccesary whitespace.

Hint (helpful functions):
https://www.w3schools.com/python/ref_func_reversed.asp
https://www.w3schools.com/python/ref_string_split.asp
"""
def backwards(st):
    # Your Code Here
    pass

#Problem 3: recursion
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

"""
Now time to try recursion yourself:

factorials!
https://en.wikipedia.org/wiki/Factorial
"""

def fac(n):
  #First (and only?) base case:

  #Recursive case:
  pass

#Problem 4 (for next time?):
"""
Recursion with lists

"""
def head(myList):
  pass

def tail(myList):
  pass