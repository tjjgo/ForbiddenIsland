import csv
import random

TREASURE_CARD_PATH = "treasure_cards.csv"

class TreasureCard():
    def __init__(self, name, description, imageDir, canBeUsed):
        """Constructor: String, String, String, boolean -> self"""
        self.name = name
        self.description = description
        self.image = imageDir
        self.canBeUsed = canBeUsed

def initCardList(cardFile):
    """"String -> TreasureCard[]"""
    cardList = []
    with open(cardFile) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            for i in range(0, int(row[1])):
                cardList.append(TreasureCard(row[0], row[2], row[3], row[4]))
    random.shuffle(cardList)
    return cardList

cardList = initCardList(TREASURE_CARD_PATH)
discardList = []

def printCardList():
    """ -> void"""
    for i in range(0, len(cardList)):
        print(cardList[i].name, cardList[i].description, cardList[i].image, cardList[i].canBeUsed)

def pop2Cards(cardList, isInitial=False): # isInitial will mean that no waters rise cards will be returned
    """TreasureCard[], boolean -> TreasureCard[2]"""
    run = True
    cardsToAppend = []
    try:
        while True:
            card1 = cardList.pop()
            card2 = cardList.pop()
            discardList.append(card1)
            discardList.append(card2)
            if isInitial:
                if card1.name == "Waters Rise!":
                    cardsToAppend.append(card1)
                    while card1.name == "Waters Rise!":
                        cardsToAppend.append(card1)
                        card1 = cardList.pop()
                if card2.name == "Waters Rise!":
                    cardsToAppend.append(card2)
                    while card2.name == "Waters Rise!":
                        cardsToAppend.append(card2)
                        card2 = cardList.pop()
                for card in cardsToAppend:
                    cardList.append(card)
                    random.shuffle(cardList)
            return [card1, card2]
    except: # empty list
        for card in discardList:
            cardList.append(card)
        random.shuffle(cardList)
        print("retry")
        return pop2Cards(cardList, isInitial)


"""
#test loop
while True:
    for i in pop2Cards(cardList, False):
        print(i.name)
    print("done")
"""
