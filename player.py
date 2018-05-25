# Include asset handling

class Player:
    def __init__(self):
        """Constructor: -> self"""
        self.adventurer = None # AdventurerCard
        self.treasureCards = [] # TreasureCard[5]
        self.actionsRem = 3
        self.treasures = []
        self.isTurn = False
        self.position = 0 # Do we use indexing or what, cos then problem with moving
        self.icon = None
        self.id = None
    def setAdventurer(self, adventurer):
        """AdventurerCard -> void"""
        self.adventurer = adventurer
    def addTreasureCard(self, card):
        """TreasureCard -> void"""
        self.treasures += [card]
    def setPosition(self, index):
        """int -> void"""
        self.position = x+y*1j
    def move(self, dX, dY):
        """int, int -> void"""
        self.position += (dx+dy*1j)
    def setIcon(self, imgDir):
        """String -> void"""
        self.icon = getImg(imgDir)
    def setId(self, _id):
        """int -> void"""
        self.id = _id
    def getActions(self):
        """ -> int"""
        return self.actionsRem
    def getAdventurer(self):
        """ -> AdventurerCard"""
        return self.adventurer
    def getPosition(self):
        """ -> int"""
        return self.position
    def getId(self):
        """ -> int"""
        return self.id
    def getTreasureCards(self):
        """ -> TreasureCard[]"""
        return self.treasureCards
