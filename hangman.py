#start of game

print("Time to play Hangman!")

#ask user for input and enter spaces

word = list(input("What word would you like to be guessed? "))
print("\n" * 30)

length = len(word)

#make empty list for underscores and fill with lines according to length
#make empty list for previous guessse

guess_word = []

guesses = []

for i in range(length):
    guess_word.append("_ ")

print(guess_word)

#until guessed word is equal to word, ask user for letter and check in list

while guess_word != word:

    letter = input("Guess a letter! ")

    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                guess_word[i] = letter

    if letter not in word:
        guesses.append(letter)
        print(guesses)
        print("    ")
        print("Try again!")

    print(guess_word)
    print("    ")

#end the game

print("You guessed the word! Thanks for playing! \^.^/ ")
