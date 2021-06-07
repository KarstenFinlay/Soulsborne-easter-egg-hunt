import pandas as pd

armour = './data/DemonSouls/armour.csv'
key_items = './data/DemonSouls/key_items.csv'
rings = './data/DemonSouls/rings.csv'
spells = './data/DemonSouls/spells.csv'
weapons = './data/DemonSouls/weapons.csv'

files = []

answer_to_armour = input("Would you like armour? Y/N\n").capitalize()
answer_to_key_items = input("Would you like key items? Y/N\n").capitalize()
answer_to_rings = input("Would you like rings? Y/N\n").capitalize()
answer_to_spells = input("Would you like spells? Y/N\n").capitalize()
answer_to_weapons = input("Would you like weapons? Y/N\n").capitalize()

if answer_to_armour == "Y":
    files.append(armour)

if answer_to_key_items == "Y":
    files.append(key_items)

if answer_to_rings == "Y":
    files.append(rings)

if answer_to_spells == "Y":
    files.append(spells)

if answer_to_weapons == "Y":
    files.append(weapons)

if not files:
    print("No options selected")
else:
    all_items = pd.concat([pd.read_csv(f) for f in files])

    all_items.to_csv("all_items.csv", index=False, encoding='utf-8-sig')

    data = pd.read_csv("all_items.csv")

    print(data['NAME'].sample(n=10).to_string())
