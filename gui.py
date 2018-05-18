try: import Tkinter as Tk
except ImportError: import tkinter as Tk

class App():
    SIZE = 800
    TILE_SIZE = 80
    def __init__(self):
        self.root = Tk.Tk()
        self.root.title("Forbidden Island")
        self.root.geometry("{0}x{0}".format(self.SIZE))
        self.root.resizable(0,0)
        self.canvas = Tk.Canvas(self.root, width=self.SIZE, height=self.SIZE, bg="#705840")
        self.canvas.pack()
    mainloop = lambda self: self.root.mainloop()
    def drawRect(self, x1,y1, x2,y2):
        self.canvas.create_rectangle(x1,y1, x2,y2, fill="DARK GREY")
    def addTile(self, x, y):
        pass
    def addTiles(self):
        spacing = (self.SIZE-(self.TILE_SIZE*8))/9.0
        for y in range(6):
            yPos = self.TILE_SIZE*(y+1) + spacing*(y+2)
            n = int(7-2*abs(2.5-y)) #2,4,6,6,4,2
            xOffset = int(-0.5+abs(2.5-y)) # 2,1,0,0,1,2
            for x in range(n):
                xPos = self.TILE_SIZE*(x+1+xOffset) + spacing*(x+2+xOffset)
                self.drawRect(xPos,yPos, xPos+self.TILE_SIZE, yPos+self.TILE_SIZE)
            
        

root = App()
root.addTiles()
root.mainloop()
