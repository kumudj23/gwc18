def combine(firstWord, firstLength, secondWord, secondLength):
    firstWord = firstWord[ :firstLength]
    secondLength = len(secondWord) - secondLength
    secondWord = secondWord[secondLength: ]
    finalWord = firstWord + secondWord
    return finalWord

def main():
    print("Time to go and make a portmanteau!")
    oneWord = input("First word: ")
    oneLength = int(input("Length of first slice: "))
    twoWord = input("Second word: ")
    twoLength = int(input("Length of the second slice: "))
    print(combine(oneWord, oneLength, twoWord, twoLength))

if __name__ == '__main__':
    main()
