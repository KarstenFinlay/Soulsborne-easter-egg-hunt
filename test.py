import pandas as pd

armour = pd.read_csv('./data/DemonSouls/armour.csv', index_col=0)

print(armour)

print(armour[armour.DLC != 1].to_string())

print(armour[armour.COVENANT != 1].to_string())
