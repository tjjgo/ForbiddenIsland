import random

class FloodCard():
    """

    Multi-purpose class for manipulation and access of flood cards

    """

    FLOOD_CARDS_PATH = "flood_cards.csv"

    def __init__(self):
        "-> void"

        self.flood_level = 2 #To get from other object


        self.flood_cards = []
        self.turn_cards = []

        for i in list(open(self.FLOOD_CARDS_PATH, 'r').readlines()):
            self.flood_cards.append(i.replace("\n", "").split(","))

        random.shuffle(self.flood_cards)

    #General functions
    def getFloodCards(self, n, is_waters_rise=False):
        "int* -> array"

        selected_cards = self.flood_cards[:n] #select top n shuffled cards
        self.turn_cards += selected_cards

        del self.flood_cards[:n]

        if is_waters_rise:
            random.shuffle(self.turn_cards)
            self.flood_cards = self.turn_cards + self.flood_cards
        else:
            self.flood_cards += self.turn_cards

        return selected_cards

    #Game functions
    def getInitialFloodCards(self):
        "-> array"
        return self.getFloodCards(6)


    def watersRiseEvent(self):
        "-> array"
        return self.getFloodCards(self.flood_level, True)


    def shuffleAllFloodCards(self):
        "-> array"
        random.shuffle(self.flood_cards)
        return self.flood_cards


    #Debug functions
    def printFloodCardInfo(self):
        "-> void"

        print(self.flood_cards)
        print(self.turn_cards)
