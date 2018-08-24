import json

keys = ["Name", "Birthplace", "Age", "Favorite Ice Cream Flavor", "Number of Siblings"]
questions = ["What is your name? ", "Where were you born? ", "How old are you? ", "What is your favorite ice cream flavor? ", "How many siblings do you have? "]
listOfDictionaries = []

while True:
    questions_and_answers = {}
    for i in range(len(questions)):
        questions_and_answers[keys[i]] = input(questions[i])
    listOfDictionaries.append(questions_and_answers)

    check = input("Do you want to continue adding responses? ")
    if check == "yes":
        continue
    else:
        break

print("Thanks!")

f = open("answers.json", "r")
old_responses = json.load(f)
listOfDictionaries.extend(old_responses)
print(old_responses)
f.close()

f = open("answers.json", "w")
json.dump(listOfDictionaries, f)
f.close()
