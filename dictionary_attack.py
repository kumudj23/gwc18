def checkdict(password, words):
    if password in words:
        return True
    else:
        return False

def removeSubs(password):
    number_check = {
        "4" : "a",
        "0" : "o",
        "3" : "e",
        "1" : "l",
        "5" : "s",
        "6" : "g",
        "2" : "z"
    }

    for character in password:
        if character in number_check.keys():
            password = password.replace(character, number_check[character])
        else:
            continue

    return password

def numbersAway(password):
    for i in range(len(password)):
        if password[i].isdigit():
            if password[i:].isdigit():
                return password[:i]
    return False

def twoWords(password, words):
    for i in range(1,len(password)):
        if password[:i] in words and password[i:] in words:
            return True, password[:i], password[i:]

def main():
    #Opens a file. You can now look at each line in the file individually with a statement like "for line in f:
    f = open("dictionary.txt","r")

    print("Can your password survive a dictionary attack?")

    #Take input from the keyboard, storing in the variable test_password
    #NOTE - You will have to use .strip() to strip whitespace and newlines from the file and passwords

    test_password = input("Type in a trial password: ")

    #Write logic to see if the password is in the dictionary file below here:

    words = []

    #make loop to add possible passwords to a list

    for line in f:
        line = line.strip()
        words.append(line)

    f.close()
    first = removeSubs(test_password)
    second = numbersAway(test_password)

    if checkdict(second, words) or checkdict(first, words) or checkdict(test_password, words) or twoWords(test_password, words):
        print("Bad password.")
    else:
        print("Nice job!")
    # first_password = removeSubs(test_password)
    # if not checkdict(first_password, words):
    #     second_password = numbersAway(test_password)
    #     if checkdict(second_password, words):
    #         print("Bad password.")
    #     else:
    #         print("Nice job!")
    # else:
    #      print("Bad password.")

if __name__ == "__main__":
    main()
