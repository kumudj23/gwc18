"""Gets band color for a value according to the standard color code scheme for 4-band resistors

    Params:
    - value: an integer that indicates which color is to be returned from the scheme

    Returns: A string representing the color for a band
"""
def getColor(value):
    colors = ["black", "brown", "red", "orange", "yellow", "green", "blue", "purple", "gray", "white"]
    return colors[value]

"""Gets multiplying factor for a given resistance number

    Params:
    - resistance: an integer that represents the resistance (in ohms)

    Returns: A integer representing the multiplying factor as a power of 10
    (e.g. 2 is returned as the power of 10 when the multiply factor is 100)
"""
def getMultiplyingFactor(resistance):
    multiply = str(resistance)

    if len(multiply) <= 2:
        return 0
    return multiply[2:].count("0")

"""Determines the color coding sequence for a resistor

    Params:
    - resistance: an integer that represents the resistance (in ohms)

    Returns: A list of colors representing the color coded sequence for the given resistance
"""
def getSequence(resistance):

    if len(str(resistance)) > 2 and resistance % 10 != 0:
        print("Error! Invalid input.")

    finalList = []

    finalList.append(getColor(int(str(resistance)[0])))
    finalList.append(getColor(int(str(resistance)[1])))
    finalList.append(getColor(getMultiplyingFactor(resistance)))

    return finalList

def testEquality(resistance, expected):

    calculated = getSequence(resistance)

    if calculated == expected:
        print("Test case for " + str(resistance) + " passed.")
    else:
        print("Test case for " + str(resistance) + " failed.")
        print("got ", calculated, "expected ", expected)

def main():
    getSequence(999)

if __name__ == '__main__':
    main()
