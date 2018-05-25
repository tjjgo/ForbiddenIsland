#--------------------------------Imports---------------------------------------#
try: import Tkinter as Tk
except ImportError: import tkinter as Tk

import os
if False:
    import gameScreen

#------------------------------Root--------------------------------------------#
root = Tk.Tk()
root.title("Forbidden Island")
root.attributes("-fullscreen", True)

root.update()
WIDTH = int(root.winfo_screenwidth())
HEIGHT = int(root.winfo_screenheight())

welcomeFrame = Tk.Frame(root, width=WIDTH, height=HEIGHT)
welcomeFrame.pack(anchor=Tk.CENTER)

#----------------------------------Functions-----------------------------------#
def play_the_game():
    welcomeFrame.destroy()

    # TODO: Brings down options for

def open_rulebook():
    os.chdir("./Assets")
    os.startfile("ForbiddenIslandTM-RULES.pdf")

"""def canvasEvent(e):
    def isInBox(e, x1,y1, x2,y2):
        return False
    if isInBox(e, 100,100, 125,125):
        play_the_game()
    elif isInBox(e, 150,150, 175,175):
        open_rulebook()
    else:
        print("Invalid pos")
    print(e.keysym)"""

#-------------------------------Background Image-------------------------------#
canvas = Tk.Canvas(welcomeFrame)
canvas.place(relx=0, rely=0, relwidth=1.0, relheight=1.0)

bgImg = Tk.PhotoImage(file="Assets/new_background.png") # 1024x715
# TODO: Resize later in photoshop
canvas.create_image(WIDTH//2, HEIGHT//2, image=bgImg)

#------------------------------------Buttons-----------------------------------#
#playRect = canvas.create_rectangle(100,100, 150,150, tags=["action", "play"])
#ruleRect = canvas.create_rectangle(200,200, 250,250, tags=["action", "rules"])

#canvas.tag_bind(playRect, "<Button-1>", play_the_game)
#canvas.tag_bind(ruleRect, "<Button-1>", open_rulebook)
#canvas.bind("<Button-1>", canvasEvent)


play_button = Tk.Button(welcomeFrame, text="Play", command=play_the_game)
play_button.place(relx=0.5,rely=0.5 , relwidth=0.1,relheight=0.1) # Align up with img

rulebook_button = Tk.Button(welcomeFrame, text="Rulebook", command=open_rulebook)
rulebook_button.place(relx=0.5,rely=0.8 , relwidth=0.1,relheight=0.1) # Align up with img

#difficulty = Tk.StringVar(welcomeFrame)
#difficulty.set("Novice")
#difficulty_button = Tk.OptionMenu(welcomeFrame, difficulty, "Novice", "Normal", "Elite", "Legendary")
#difficulty_button.place(relx=0.33,rely=0.67 , relwidth=0.1,relheight=0.08)
#------------------------------Main Program------------------------------------#
root.mainloop()
