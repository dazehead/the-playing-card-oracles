# retrieving Card Data and organizing it into list
# unicode spade: 2660
# unicdoe diamond: U+25C6
# unicode club: U+2663
# unicode heart: U+1f60d
import csv
with open("Card data.csv", newline='') as card_data:
    cards = csv.reader(card_data, delimiter= ',')
    card_dict_temp = {}
    card_description = {}
    card_name = {}
    for row in cards:
        card_dict_temp.update({row[0]: [row[1], [row[2].split(';')]]})
    for x in card_dict_temp:
        card_description.update({x: []})
        for l in card_dict_temp[x][1][0]:
            card_description[x].append(l)
    for x in card_dict_temp:
        card_name.update({x: card_dict_temp[x][0]})

#print(card_name)
#print(card_description["2 Clubs"][1])

    