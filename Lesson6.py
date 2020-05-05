#Lesson 6, with Keeton

#Hey guys! Today we're going to practice our use of loops
#and list manipulations to tackle some practice problems. 

print("Question 1")
"""
You were camping with your friends far away from home, but when it's time to go back, you realize that you fuel is running out and the nearest pump is 50 miles away! You know that on average, your car runs on about 25 miles per gallon. There are 2 gallons left. Considering these factors, write a function that tells you if it is possible to get to the pump or not. Function should return true if it is possible and false if not. The input values are always positive.
"""

def zero_fuel(distance_to_pump, mpg, fuel_left):
    #Happy Coding!
    distanceCanGo = mpg * fuel_left
    if distanceCanGo == distance_to_pump:
      return True
    elif distance_to_pump > distanceCanGo:
      return False
    elif distance_to_pump < distanceCanGo:
      return True

#zero_fuel(50, 25, 2) = True
print(zero_fuel(50, 25, 2))
print(zero_fuel(100, 50, 1))

print("Question 2")
"""
You are given an array (a list) with positive numbers and a number N. You should find the N-th power of the element in the array with the index N. If N is outside of the array, then return -1. Don't forget that the first element has the index 0.
"""

def nthPower(array, n):
  index= n
  rookidee = array[n]
  return rookidee ** n
#nthPower([1, 2, 3, 4],2) = 9
print(nthPower([1, 2, 3, 4],2))
#nthPower([1, 3, 10, 100],3) = 1000000

print("Question 3")
"""
Aliens from Kepler 27b have immigrated to Earth! They have learned English and go to our stores, eat our food, dress like us, ride Ubers, use Google, etc. However, they speak English a little differently. Can you write a program that converts their Alien English to our English?

Write a function converting their speech to ours. They tend to speak the letter a like o and o like a u.
"""

def convert(st):
    # Code here
    pass

#convert('Keeton Martin') = 'Keetun Mortin'
print(convert('Keeton Martin'))
#convert('hello') = 'hellu'

print("Question 4")
"""
Your task is to find the first element of a list that is not consecutive.

By not consecutive we mean not exactly 1 larger than the previous element of the list.

E.g. If we have a list [1,2,3,4,6,7,8] then 1 then 2 then 3 then 4 are all consecutive but 6 is not, so that's the first non-consecutive number.

If the whole list is consecutive then return null.
"""
def first_non_consecutive(arr):
    #your code here
    pass

#first_non_consecutive([1,2,3,4,6,7,8]) = 6
print(first_non_consecutive([1,2,3,4,6,7,8]))
#first_non_consecutive([1,2,3,4,5,6,7,8]) = None
#first_non_consecutive([4,6,7,8,9,11]) = 6
#first_non_consecutive([4,5,6,7,8,9,11]) = 11
#first_non_consecutive([-3,-2,0,1]) = 0

