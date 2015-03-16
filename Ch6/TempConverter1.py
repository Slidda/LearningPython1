# Temp Converter Script - Functions
def tempConvert(temp, unit):
    
    if unit == "F":
        tempReturn = (int(temp) - 32) * 5 / 9
        unitID = "C"
    elif unit == "C":
        tempReturn = (int(temp) * (9 / 5)) + 32
        unitID = "F"
    else:
        tempReturn = "ERROR"
        unitID = "ERROR"
    tempConvertTuple = (tempReturn, unitID)
    return tempConvertTuple

def main():

    userInputTemp = input("input temp:")
    userInputUnit = input("input unit:")

    outputTuple = tempConvert(userInputTemp, userInputUnit)
    print(userInputTemp, "degrees", userInputUnit, "=", outputTuple[0], "degrees", outputTuple[1])
    #print(userInputTemp, "degrees", userInputUnit, "=", "{0} degrees {1}.".format(tempFtoC(userInputTemp, userInputUnit)))
    #print ("ok")
    #print(userInputTemp, "degrees", userInputUnit, "=", tempReturn, "degrees", unitID)

main()
