try: import Tkinter as Tk
except ImportError: import tkinter as Tk

class App():
    WIDTH = 1100 # > 8*TILE_SIZE
    HEIGHT = 0 # For auto height from width, keep small
    TILE_SIZE = 125 # Default=125
    
    def __init__(self):
        self.fixSize()
        self.createGui()

    def fixSize(self):
        spacingX = (self.WIDTH-(self.TILE_SIZE*8))/9.0
        spacingY = (self.HEIGHT-(self.TILE_SIZE*8))/9.0
        if ((spacingX > spacingY)and(spacingY>0)): # Height restrict
            self.SPACING = spacingY
            self.WIDTH = int(0.5+(7*self.SPACING)+(5*self.TILE_SIZE))
        else: # Width restrict
            self.SPACING = spacingX
            self.HEIGHT = int(0.5+(7*self.SPACING)+(6*self.TILE_SIZE))

    def createGui(self):
        self.root = Tk.Tk()
        self.root.title("Forbidden Island")

        self.SCREEN_WIDTH = int(self.root.winfo_screenwidth())
        self.SCREEN_HEIGHT = int(self.root.winfo_screenheight())
        self.root.geometry("{0}x{1}+{2}+{3}".format(self.WIDTH, self.HEIGHT, (self.SCREEN_WIDTH-self.WIDTH)//2, (self.SCREEN_HEIGHT-self.HEIGHT)//2))
        self.root.resizable(0,0)

        self.canvas = Tk.Canvas(self.root, width=self.WIDTH, height=self.HEIGHT, bg="#705840")
        self.canvas.pack()
        
    mainloop = lambda self: self.root.mainloop()

    def drawRect(self, x1,y1, x2,y2):
        self.canvas.create_rectangle(x1,y1, x2,y2, fill="DARK GREY")

    def addTile(self, x, y):
        xPos = self.TILE_SIZE*x + self.SPACING*(x+1)
        yPos = self.TILE_SIZE*y + self.SPACING*(y+1)
        self.drawRect(xPos,yPos, xPos+self.TILE_SIZE, yPos+self.TILE_SIZE)

    def addTiles(self):
        spacing = self.SPACING
        for y in range(6):
            #yPos = self.TILE_SIZE*(y+1) + spacing*(y+2)
            n = int(7-2*abs(2.5-y)) #2,4,6,6,4,2
            xOffset = 1+int(-0.5+abs(2.5-y)) # 2,1,0,0,1,2
            for x in range(n):
                self.addTile(x+xOffset, y)

root = App()
root.addTiles()
root.mainloop()
