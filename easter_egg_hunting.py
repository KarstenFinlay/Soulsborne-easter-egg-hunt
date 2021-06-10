import pandas as pd
import sys

game_choices = ["DemonSouls", "DarkSouls", "DarkSouls2", "Bloodborne", "DarkSouls3", "Sekiro"]

game_choice = input("Please select which game you wish to have an easter egg hunt in:\n1. Demon Souls\n2. Dark Souls\n3. Dark Souls 2\n4. Bloodborne\n5. Dark Souls 3\n6. Sekiro\n")

while True:
    try:
        game_choice_index = int(game_choice) - 1

        if game_choice_index < 0:
            game_choice = input("Options must be an interger of one or higher:\n")
            continue

        game = game_choices[game_choice_index]
        break
    except ValueError:
        game_choice = input("That is not a valid choice, please input a number:\n")
    except IndexError:
        game_choice = input("Please select one of the valid options:\n")

