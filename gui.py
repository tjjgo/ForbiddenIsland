try: import Tkinter as Tk
except ImportError: import tkinter as Tk

class App():
    WIDTH = 1100 # > 8*ISLAND_SIZE
    HEIGHT = 0 # For auto height from width, keep small
    ISLAND_SIZE = 125 # Default=125

    def __init__(self):
        """Constructor: -> self"""
        self.fixSize()
        self.createGui()

    def fixSize(self):
        """ -> void"""
        spacingX = (self.WIDTH-(self.ISLAND_SIZE*8))/9.0
        spacingY = (self.HEIGHT-(self.ISLAND_SIZE*8))/9.0
        if ((spacingX > spacingY)and(spacingY>0)): # Height restrict
            self.SPACING = spacingY
            self.WIDTH = int(0.5+(7*self.SPACING)+(5*self.TILE_SIZE))
        else: # Width restrict
            self.SPACING = spacingX
            self.HEIGHT = int(0.5+(7*self.SPACING)+(6*self.TILE_SIZE))

    def createGui(self):
        """ -> void"""
        self.root = Tk.Tk()
        self.root.title("Forbidden Island")

        self.SCREEN_WIDTH = int(self.root.winfo_screenwidth())
        self.SCREEN_HEIGHT = int(self.root.winfo_screenheight())
        self.root.geometry("{0}x{1}+{2}+{3}".format(self.WIDTH, self.HEIGHT, (self.SCREEN_WIDTH-self.WIDTH)//2, (self.SCREEN_HEIGHT-self.HEIGHT)//2))
        self.root.resizable(0,0)

        self.canvas = Tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg="#705840")
        self.canvas.pack()

    def drawRect(self, x1,y1, x2,y2):
        """double, double, double, double -> void"""
        self.canvas.create_rectangle(x1,y1, x2,y2, fill="DARK GREY")

    def addIsland(self, x, y):
        """double, double -> void"""
        xPos = self.ISLAND_SIZE*x + self.SPACING*(x+1)
        yPos = self.ISLAND_SIZE*y + self.SPACING*(y+1)
        self.drawRect(xPos,yPos, xPos+self.ISLAND_SIZE, yPos+self.ISLAND_SIZE)

    def addIslandss(self):
        """ -> void"""
        for y in range(6):
            n = int(7-2*abs(2.5-y)) # Number of islands to gen in row # 2,4,6,6,4,2
            xOffset = int(0.5+abs(2.5-y)) # Offset to create * shape # 3,2,1,1,2,3
            for x in range(n):
                self.addIsland(x+xOffset, y)

    mainloop = lambda self: self.root.mainloop()
    
root = App()
root.addIsland()
root.mainloop()
