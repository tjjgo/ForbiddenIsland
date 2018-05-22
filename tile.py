try: import Tkinter as Tk
except ImportError: import tkinter as Tk

class Tile():
    def __init__(self, name, bgImgDir):
        """Constructor: String, String -> self"""
        # TODO: Implement, and add params
        self.flooded = False
        self.name = name
        self.bgImgDir = bgImgDir
    def getName(self):
        """ -> String"""
        return self.name
    def getPhotoImage(self):
        """ -> Tk.PhotoImage"""
        return Tk.PhotoImage(file=self.bgImgDir)