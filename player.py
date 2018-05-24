class Player:
    def __init__(self):
        """Constructor: -> self"""
        self.special = None #
        self.treasureCards = [] # Max 5
        self.actionsRem = 3
        self.treasures = []
        self.isTurn = False
        self.position = (0,0)
    def setSpecial(self, card):
        """AdventurerCard -> void"""
        self.special = card
    def addTreasureCard(self, card):
        """TreasureCard -> void"""
