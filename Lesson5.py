#Lesson 5, with Keeton

#To Begin: What did we talk about last time?

#Next: Review the Mini-Homework1. Did anyone get some solutions?

#Today's focus: Python Lists

print("\n Section 1: Intro to lists")
#A list is a kind of collection of variables.
#Specifically, a list is ordered an changeable. 

thislist = ["apple", "banana", "cherry"]
print(thislist)

#Accessing the list items.

listOfPokemon = ["Bulbasaur", "Charmander", "Squirtle", "burrito"]
print(listOfPokemon[0])
print(listOfPokemon[-3])

#In computer science and programming, we always start counting at 0. 
#The number in the square brackets indicating which element in the list we want is called:
#index

#What happens when the index is negative? (Raise your hand)

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango","people who ate a watermellon with the seeds in it" ]

#What if you want only a section of the list?
print(fruits[2:5])
#Note: The search will start at index 2 (included) and end at index 5 (not included).

print("\n Section 2: Lists of Ints ")

#What about other ways to make lists. Does this look familiar?
someNumbers = range(1, 10)

#let's make sure it's a technically a list
someNumbers = list(someNumbers)

print(someNumbers)

#What will the below line print? (Raise your hand)
# print(someNumbers[4])

#We can change elements of a list:
someNumbers[4] = 200
print(someNumbers)

print("\n Section 3: Make your own lists ")

#Create a list of colors, and print it
colors = ["burrito brown", "burrito blue", "ree red"]
print(colors)
#Create a list of videogames, and print it
games = ["minecraft", "roblox", "Super smash bros", "FORTNITE BAD"]
print(games)
print("\n Section 4: List Length and Adding Items ")

print("Our fruits list again: ", fruits)
print("Our fruits lists is this long: ", len(fruits))

#Let's make it even longer!
fruits.append("peach")
print("Our fruits list again: ", fruits)
print("Our fruits lists is this long: ", len(fruits))

#Now use .append() to add a color to your list
fruits.append("burrito brown")
#And print the length of the new list of colors
len(fruits)
print("\n Section 5: loops and lists")

for thing in fruits:
	print(thing)
print(fruits)
#How is this different than print(fruits)? Raise your hand

#If you did the mini-homework, copy and paste your addExclamation function here:
def addExclamation(EXL):
  return EXL + "!"


shinyThings = []
for thing in fruits:
	shinyThings.append(addExclamation(thing))
print(shinyThings)

print("\n Section 6 (Challenge): Head and Tail")

print("\n Section 7 (Challenge): lists of lists")