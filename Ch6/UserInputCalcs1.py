userInputBase = input("Enter a base:") # User inputs base.
userInputExponent = input("Enter an exponent:") # User inputs exponent.
floatBase = float(userInputBase) # Changes string to float.
floatExponent = float(userInputExponent)
userOutputResult = float(floatBase ** floatExponent) # Result = Base ^ Exponent.
print(userInputBase, "to the power of", userInputExponent, "=", userOutputResult)
