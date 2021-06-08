import pandas as pd
import sys

game_choice = input("Please select which game you wish to have an easter egg hunt in:\n1. Demon Souls\n2. Dark Souls\n3. Dark Souls 2\n4. Bloodborne\n5. Dark Souls 3\n6. Sekiro\n")

if game_choice == "1":
    game = "DemonSouls"
elif game_choice == "2":
    game = "DarkSouls"
elif game_choice == "3":
    game = "DarkSouls2"
elif game_choice == "4":
    game = "Bloodborne"
elif game_choice == "5":
    game = "DarkSouls3"
elif game_choice == "6":
    game = "Sekiro"
else:
    sys.exit("No option selected")

armour = f'./data/{game}/armour.csv'
blood_gems = './data/Bloodborne/blood_gems.csv'
chalices = './data/Bloodborne/chalices.csv'
hunter_tools = './data/Bloodborne/hunter_tools.csv'
key_items = f'./data/{game}/key_items.csv'
rings = f'./data/{game}/rings.csv'
runes = './data/Bloodborne/runes.csv'
spells = f'./data/{game}/spells.csv'
weapons = f'./data/{game}/weapons.csv'

files = []

answer_to_all_items = input("Would you like every item to be included? Y/N\n").capitalize()

if answer_to_all_items == "Y":
    files.append(key_items)
    
    if game != "Sekiro":
        files.append(armour)
        files.append(weapons)

    if game != "Bloodborne" and game != "Sekiro":
        files.append(rings)
        files.append(spells)

    if game == "Bloodborne":
        files.append(blood_gems)
        files.append(chalices)
        files.append(hunter_tools)
        files.append(runes)
else:
    answer_to_key_items = input("Would you like key items? Y/N\n").capitalize()

    if game != "Sekiro":
        answer_to_armour = input("Would you like armour? Y/N\n").capitalize()
        answer_to_weapons = input("Would you like weapons? Y/N\n").capitalize()

    if game != "Bloodborne" and game != "Sekiro":
        answer_to_rings = input("Would you like rings? Y/N\n").capitalize()
        answer_to_spells = input("Would you like spells? Y/N\n").capitalize()

    if game == "Bloodborne":
        answer_to_rings = "N"
        answer_to_spells = "N"
        answer_to_blood_gems = input("Would you like blood gems? Y/N\n").capitalize()
        answer_to_chalices = input("Would you like chalices? Y/N\n").capitalize()
        answer_to_hunter_tools = input("Would you like hunter_tools? Y/N\n").capitalize()
        answer_to_runes = input("Would you like runes? Y/N\n").capitalize()
    
    if answer_to_key_items == "Y":
        files.append(key_items)

    if answer_to_armour == "Y":
        files.append(armour)

    if answer_to_weapons == "Y":
        files.append(weapons)

    if answer_to_rings == "Y":
        files.append(rings)

    if answer_to_spells == "Y":
        files.append(spells)

    if answer_to_blood_gems == "Y":
        files.append(blood_gems)

    if answer_to_chalices == "Y":
        files.append(chalices)

    if answer_to_hunter_tools == "Y":
        files.append(hunter_tools)

    if answer_to_runes == "Y":
        files.append(runes)


if not files:
    print("No options selected")
else:
    all_items = pd.concat([pd.read_csv(f) for f in files])

    all_items.to_csv("all_items.csv", index=False, encoding='utf-8-sig')

    data = pd.read_csv("all_items.csv", index_col="NAME")

    print(data.sample(n=10).to_string())
