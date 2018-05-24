import random
class FloodCard():

    FLOOD_CARDS_PATH = "flood_cards.csv"

    def __init__(self):
        self.flood_cards = []
        for i in list(open(self.FLOOD_CARDS_PATH, 'r').readlines()): self.flood_cards.append(i.replace("\n", ""))
        print(flood_cards)

    def initial_sinking(self):
        "To do"


app = FloodCard()
