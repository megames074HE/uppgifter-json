import json
import random

random_number = random.randint(1, 50)
guesses = 0

with open("highscores.json", "r", encoding="utf-8") as file:
    highscores = json.load(file)

highscores['scores'].sort(key=lambda item: item["guesses"])

print("Highscores:")
for player in range(3):
    highscore_name = highscores['scores'][player]['name']
    highscore_guesses = highscores['scores'][player]['guesses']
    print(f"spelare {highscore_name} med {highscore_guesses} gissningar")

name = input("\nVad heter du: ")

while True:
    guessed_number = int(input("Gissa: "))
    guesses += 1
    if guessed_number == random_number:
        print(f"Di gissade numret. Det tog {guesses} gissningar")
        break

if guesses < highscores['scores'][4]['guesses']:
    highscores['scores'].pop(4)
    highscores['scores'].append({"name": name, "guesses": guesses})

if guesses < highscores['scores'][2]['guesses']:
    print("Du hamnade i top 3")


with open("highscores.json", "w", encoding="utf-8") as file:
    json.dump(highscores, file, indent=2, ensure_ascii=False)
