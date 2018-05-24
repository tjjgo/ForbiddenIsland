import random

#Flood cards
class FloodCard():

    FLOOD_CARDS_PATH = "flood_cards.csv"

    def __init__(self):
        "-> void"

        self.flood_cards = []

        for i in list(open(self.FLOOD_CARDS_PATH, 'r').readlines()):
            self.flood_cards.append(i.replace("\n", "").split(","))


    def initial_sinking(self):
        "-> void"

        temp_cards = self.flood_cards
        random.shuffle(temp_cards)
        selected_cards = temp_cards[0:6] #select top 6 shuffled cards

        print(selected_cards)


app = FloodCard()

for i in range(100):
    app.initial_sinking()
