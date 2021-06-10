import pandas as pd
import sys

from os import listdir

def question_yes_no(question):
    answer = input(question).capitalize()
    while True:
        if answer != "Y" and answer != "N":
            answewr = input("Please input Y or N\n")
            continue

        return answer == "Y"

def question_number(question):
    answer = input(question)
    while True:
        try:
            return int(answer)
        except ValueError:
            answer = input("Your answer must be an integer:\n")

game_choices = ["DemonSouls", "DarkSouls", "DarkSouls2", "Bloodborne", "DarkSouls3", "Sekiro"]

while True:
    try:
        game_choice_index = question_number("Please select which game you wish to have an easter egg hunt in:\n1. Demon Souls\n2. Dark Souls\n3. Dark Souls 2\n4. Bloodborne\n5. Dark Souls 3\n6. Sekiro\n") - 1

        if game_choice_index < 0:
            game_choice = input("Options must be an integer of one or higher:\n")
            continue

        game = game_choices[game_choice_index]
        break
    except IndexError:
        game_choice = input("Please select one of the valid options:\n")

game_files = listdir(f"./data/{game}")

all_items_answer = question_yes_no("Would you like every item type to be included? Y/N\n")

easter_egg_items = pd.DataFrame()

for file in game_files:
    if not all_items_answer and not question_yes_no(f"Would you like {file} to be included? Y/N\n"):
        continue

    data = pd.read_csv(f"./data/{game}/{file}")

    max_items = len(data.index)

    while True:
        quantity = question_number(f"How many items from {file} would you like to hunt? (0 - {max_items})\n")
        
        if quantity > max_items:
            print(f"Quantity selected is greater than number of available items within {file} ({max_items})")
            continue

        if quantity >= 0:
            break

        print("Selected quantity must be positive.")

    easter_egg_items = easter_egg_items.append(data.sample(n=quantity))

print(easter_egg_items.to_string())

### CHALLENGES

# 1. Getting all file names for game [X]

# 2. Filtering files [X]

# 3. Read each file indivdually [X]

# 4. Filter other colums

# 5. Sample selected amount for each file

# 6. Print out user's easter egg hunt list and write to file