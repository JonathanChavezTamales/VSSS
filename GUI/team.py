import tkinter as tk
from tkinter import ttk
from robot import Robot
from PIL import ImageTk,Image

class Team(ttk.Frame):
    def __init__(self, parent, height, width, isEnemyTeam):
        super().__init__(parent)

        self.height = int(height/3)
        self.width = int(width)

        # self["padding"] = (20, 20, 20, 20)
        self["height"] = self.height
        self["width"] = self.width
        self["style"] = style="BackgroundGREEN.TFrame" if isEnemyTeam else "BackgroundORANGE.TFrame"
    

        # robot1 = Robot(self, height=height, width=width)
        # robot1.grid(row=0, column=0, sticky="NSEW")

        # robot1 = Robot(self, height=height, width=width)
        # robot1.grid(row=0, column=1, sticky="NSEW")

        # robot1 = Robot(self, height=height, width=width)
        # robot1.grid(row=0, column=2, sticky="NSEW")

        BACKGROUND_PATH = "Assets/team1_background.jpg" if isEnemyTeam else "Assets/team2_background.jpg"
        canvas= tk.Canvas(self,width=width,height=height/3)
        img = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((self.width, self.height), Image.ANTIALIAS))
        canvas.background = img  # Keep a reference in case this code is put in a function.
        bg = canvas.create_image(0, 0, anchor=tk.NW, image=img)

        canvas.grid()

    