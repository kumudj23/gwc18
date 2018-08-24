# --- Define your functions below! ---

def intro():
    print("Welcome to Chatbot!")

def greeting():
    print("Hello!")

def farewell():
    print("Talk to you later!")
    exit()

def say_default():
    print("That's cool!")

def feelings():
    print("I'm feeling good today! How about you?")

def is_valid_input(user_input, valid_responses):
    return user_input in valid_responses

def hangman():
    print("Time to play Hangman!")

    word = list(input("What word would you like to be guessed? "))
    print("\n" * 30)

    length = len(word)
    guess_word = []
    guesses = []

    for i in range(length):
        guess_word.append("_ ")

    print(guess_word)

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

    print("You guessed the word! Thanks for playing! \^.^/ ")
    print()

def meme():
    import random
    list_memes = ["(╯°□°) ╯^ ┻━┻", "¯\_(* . *)_/¯", " ‹^› ‹(•_•)› ‹^›", "t(-_-t)"]
    meme_random = random.SystemRandom()
    print(meme_random.choice(list_memes))

def process_input(response):
    greetings = ["hello", "hey", "hi", "wassup"]
    farewells = ["bye", "see ya", "goodbye"]
    emotion = ["how are you?", "how ya doin?",]
    game = ["play", "game", "play hangman", "hangman"]
    memes = ["funny", "meme", "joke", "show me memes"]
    if is_valid_input(response, greetings):
        greeting()
    elif is_valid_input(response, farewells):
        farewell()
    elif is_valid_input(response, emotion):
        feelings()
    elif is_valid_input(response, game):
        hangman()
    elif is_valid_input(response, memes):
        meme()
    else:
        say_default()

# --- Put your main program below! ---

def main():
  intro()
  while True:
    answer = input("(What will you say?) ")
    process_input(answer)


# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
  main()
