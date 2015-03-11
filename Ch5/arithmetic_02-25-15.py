print ("Check decimaliness: 5 / 2 = ", 5/2)
"""
This checks the decimal / int disparity between Python 2 and Python 3
"""

myNumber = "12"
print("string " + myNumber * 3) # Keeps it as a string.
print ("int", int(myNumber) * 3) # Boom, integer.
print ("float", float(myNumber) * 3) # Boom, float.
print ("floatstring " + str(float(myNumber) * 3)) # Tada, a "floatstring."

weight = float(0.2)
animal = "newt"

print(str(weight) + "kg is the weight of the " + animal)
print("{1}kg is the weight of the {0}.".format(animal, weight))
print("{}kg is the weight of the {}.".format(weight, animal))
print("{weight2}kg is the weight of the {animal2}.".format(animal2 = "newt", weight2 = float(0.2)))

print("Can't find me a string: ", "AAA".find("a"))

"""
Create a string object that contains the value “version 2.0”; find() the first occurrence
of the number 2.0 inside of this string by first creating a “float” object that stores the
value 2.0 as a floating-point number, then converting that object to a string using the
str() function
"""
print("Found me a string - version2.0: ", "version2.0".find(str(float(2.0))))

"""
Write and test a script that accepts user input using raw_input(), then displays the
result of trying to find() a particular letter in that input
"""
userInput = input("Tell it NOW!:")
print("Do you's have a Q in your string? '-1' means no: ", userInput.find("Q"))

userInput2 = input("Enter some text:")

userHacksor = userInput2.replace("a", "4")
userHacksor = userHacksor.replace("b", "8")
userHacksor = userHacksor.replace("e", "3")
userHacksor = userHacksor.replace("l", "1")
userHacksor = userHacksor.replace("o", "0")
userHacksor = userHacksor.replace("s", "5")
userHacksor = userHacksor.replace("t", "7")

print(userHacksor)
