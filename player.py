# Include asset handling

class Player:
    def __init__(self):
        """Constructor: -> self"""
        self.adventurer = None # AdventurerCard
        self.treasureCards = [] # TreasureCard[5]
        self.actionsRemaining = 3
        self.treasures = []
        self.isTurn = False
        self.position = (0,0)
        self.icon = None
        self.id = None

    def setAdventurer(self, adventurer):
        """AdventurerCard -> void"""
        self.adventurer = adventurer

    def addTreasureCard(self, card):
        """TreasureCard -> void"""
        if not len(self.treasures) == 5:
            self.treasures += [card]
        else:
            pass
            #Discard one card

    def setPosition(self, position):
        """int -> void"""
        self.position = position

    def move(self, dX, dY):
        """int, int -> void"""
        self.position = (self.position[0]+dX, self.position[0]+dY)

    def setIcon(self, imgDir):
        """String -> void"""
        self.icon = getImg(imgDir)

    def setId(self, _id):
        """int -> void"""
        self.id = _id

    """
    Get functions not really needed as 'object.var' is an option
    """
