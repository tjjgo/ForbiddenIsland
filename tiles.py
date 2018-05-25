try: import Tkinter as Tk
except ImportError: import tkinter as Tk

class Tile():
    def __init__(self, name, bgImgDir, cardLocation):
        """Constructor: String, String -> self"""
        self.flooded = False
        self.sunk = False # True = tile is destroyed
        self.name = name
        self.bgImgDir = bgImgDir
        self.cardLocation = cardLocation

    def getName(self):
        """ -> String"""
        return self.name

    def getPhotoImage(self):
        """ -> Tk.PhotoImage"""
        return Tk.PhotoImage(file=self.bgImgDir)

    def flood(self):
        """ -> void"""
        if not self.isFlooded():
            self.flooded = True
        else: # Destroy tile
            self.sunk = True

    def isFlooded(self):
        """ -> boolean"""
        return self.flooded

    def shore(self):
        """ -> void"""
        if not self.sunk: # Should have been GC'd but Just in Case
            self.flooded = False
