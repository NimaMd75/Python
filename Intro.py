																# 'First test'

""" The variable "check" is made here """
# check = 'Using pyhton for the first time!'
# print(check)
# number = 1+5
# print(number)
# for i in range(4,10,2):
# 	number += 1
# 	print(number + 1)

																# 'Second test'

# newList = list(range(4,10,2))

# for i in range(len(newList)):
#  print(newList[i])

																# 'Thrid test'

# def power(base,power):
# 	return base ** power

# variable = power
# base = 5
# power = 2
# print(variable(base, power))

																# 'Fourth test'

# from math import pi as piValue
# print(piValue)

 																#'Fifth test'

# def printerFunction():
# 	print('check!')
# 	# return 'Hello!'

# variable = printerFunction()
# print(variable)

																# 'sixth test'

# newTuple = "Armin" , "Nima" , "Salman"

# print(newTuple, newTuple[0])

# # if newTuple[0] == "Armin":
# 	# newTuple[3] = "Amir"

																#'Seventh test'	

# myList = [0,1,2,3,4,5,6,7,8,9,10]

# print('Third item on the list:')
# print(myList[2])
# print('Even numbers:')
# print(myList[::2])
# print('from 3rd to 5th:')
# print(myList[3:5])
# print('3 in a row:')
# print(myList[::3])
# print('reversed:')
# print(myList[::-1])
# print('from 4, 2 in a row:')
# print(myList[4::2])
# print('from 3 to 9, 3 in a row:')
# print(myList[3:9:3])
# print('to 8th:')
# print(myList[:8])

																#'Eighth test'

# cubes = [i**3 for i in range(10)]

# print(cubes)

# evenSquares = [i**2 for i in range(20) if i**2%2 == 0]

# print(evenSquares)

# bigEvens = [2*i for i in range(10*6)]

# print(bigEvens)

# del bigEvens

# bigEvens = [2*i for i in range(10**5)]

# print(bigEvens)

# bigEvens = [2*i for i in range(10**10)] #OverflowError

# bigEvens = [2*i for i in range(10**100)] #MemoryError

																# 'Ninth test'

# cubes = [i**3 for i in range(10)]

# belowTenCubes = "below 10 cubes are: {0} {1} {2}".format(cubes[0], cubes[1], cubes[2])

# print(belowTenCubes)

# print(cubes)

# cubesString = str(cubes)

# newString = "".join(cubesString)

# print(newString)

# del newString

# newString = "program is running".replace("program", "Test")

# print(newString)


																# 'Tenth test'


# def countCharacter (textName, wantedCharacter):
# 	counter = 0
# 	with open(textName, "r") as textReader:
# 		text = textReader.read()
# 		for character in text:
# 			if character == wantedCharacter:
# 				counter +=1
# 		return counter

# print(countCharacter("Notes.txt", 'r'))

																# 'Eleventh test'

# def polynomial(x):
# 	return 2*x**2 + 3*x + 5

# print(polynomial(4))

# def myFunction(function, argument):
# 	return function(argument)

# print(myFunction(lambda x: 2*x*x + 3*x + 5, 4))

# print((lambda x: 2*x**2 + 3*x + 5)(4))

# polynom = lambda x: 2*x**2 + 3*x + 5

# print(polynom(4))

																# 'Twelveth test'

# print((lambda x,y,z: x**2 + y**2 + z**2)(3,2,2))

# triple = lambda x: 3*x

# squareSums = lambda x,y,z: x**2 + y**2 + z**2

# print(squareSums(triple(1), 2, 2))

																# 'Thirteenth test'
""" Making random numbers from 10 to 20"""
# from random import randint as randomInt

# numbers = [randomInt(i, 10) for i in range(10)]

# def addTen(number):
	# return number + 10

# numbers = list(map(addTen, numbers))

# numbers = list(map(lambda x: x+10, numbers)) #same as the previous assignment

# print(numbers)
																# 'Fourteenth test'

"""Making more than 50 random even numbers"""
# from random import randint as randomInt

# numbers = [randomInt(i, 100) for i in range(100)]

# # numbers = list(filter(lambda x: x%2==0, numbers))

# def higherThanFiftyRandoms(randomsList):
# 	randomsList = list(filter(lambda x: x%2==0, randomsList))
# 	if len(randomsList) < 50:
# 		newList = [randomInt(i, 100) for i in range(100)]
# 		appendedList = higherThanFiftyRandoms(newList)
# 		for i in appendedList:
# 			randomsList.append(i)
# 	return randomsList

# numbers = higherThanFiftyRandoms(numbers)

# print("{0} \n {1}".format(len(numbers) , numbers))
																# 'Fifteenth test'

# def countdown():
# 	number = 10
# 	while number > 0:
# 		yield number
# 		number -= 1

# for i in countdown():
# 	print(i)

# def evenNumbersUpToDesired(desired):
# 	for i in range(desired):
# 		if i%2==0:
# 			yield i

# print(list(evenNumbersUpToDesired(100)))

# def makeWord(givenWord):
# 	word = ""
# 	for character in givenWord:
# 		word += character
# 		yield word

# print(list(makeWord("Ghostantanieh")))
																# 'Sixteenth test'

# def decorator(function, firstName, lastName):
# 	def wrapper():
# 		print("*******************************")
# 		function(firstName, lastName)
# 		print("*******************************")
# 	return wrapper

# def showIdentity(firstName, lastName):
# 	print("My name is: {0} {1}".format(firstName, lastName))

# decorated = decorator(showIdentity, "Nima", "Moradi")

# decorated()
																# 'Seventeenth test'

# def decorate(function):
# 	def wrapper():
# 		print("*******************************")
# 		function()
# 		print("*******************************")
# 	return wrapper

# def decorate2(function):
# 	def wrapper():
# 		print("###############################")
# 		function()
# 		print("###############################")
# 	return wrapper

# @decorate
# @decorate2
# def encourage():
# 	print("You're learning Python!")

# encourage()
																# 'Eighteenth test'
"""Working with sets"""
#sets can't have duplicated items since they're not sorted and can't be indexed
#sets use .add() instead of .append()
#methods .remove(item) and .pop() remove items from sets
# numberSet1 = {1, 2, 3, 4, 5, 6}
# numberSet2 = {4, 5, 6, 7, 8, 9}

# wordSet = set(["Hello!", "Doin fine?", "What a good day!"])

# print(len(wordSet))
# print(6 in numberSet1)
# print("What a good day!" not in wordSet)

# print(numberSet1 | numberSet2)
# print(numberSet1 & numberSet2)
# print(numberSet1 - numberSet2)
# print(numberSet2 - numberSet1)
# print(numberSet1 ^ numberSet2)

# wordSet.remove("Hello!")
# numberSet1.pop()

# print(wordSet)
# print(numberSet1)
																# 'Ninteenth test'
# from itertools import *

# startingNumber = 6
# for i in count(startingNumber):
# 	print(i)
# 	if i >=26:
# 		break
# for i in cycle("Hello!"):
# 	print(i)
# 	if i == '!':
# 		break

# for i in repeat("Bye!", 6):
# 	print(i)

"""Accumulate doesn't work on my system
summations = list(accumulate(range(10)))
print(summations)
"""

# numbers = list(range(10))
# numbers2 = list(range(10, 20))
# print(list(takewhile(lambda x: x<6, numbers)))
# print(list(chain(numbers, numbers2)))

# letters = ("A", "B", "C")
# print(list(product(letters, range(3))))
# print(list(permutations(letters)))
