import tkinter as tk
from tkinter import ttk
from robot import Robot
from PIL import ImageTk,Image
from tkinter import messagebox


class Team(ttk.Frame):
    def __init__(self, parent, height, width, isEnemyTeam):
        super().__init__(parent)

        self.height = int(height/3)
        self.width = int(width)

        #self["padding"] = (20, 20, 20, 20)
        self["height"] = self.height
        self["width"] = self.width

        self.columnconfigure(1, weight=1)
        self.rowconfigure(0, weight=1)
    
        BACKGROUND_PATH = "Assets/team1_background.jpg" if isEnemyTeam else "Assets/team2_background.jpg"
        # background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH))#.resize((self.width, int(self.height)), Image.ANTIALIAS))
        # background_label = tk.Label(self, image=background_image).place(x=0, y=0, relwidth=1, relheight=1)
        #background_label.image = background_image
        # self.background = img  # Keep a reference in case this code is put in a function.
        # bg = self.create_image(0, 0, anchor=tk.NW, image=img)

        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((self.width, self.height), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image


        self.color_picker_btn = ttk.Button(
            self,
            text="",
            #command=self.start_timer,
            cursor="hand2",
            width=self.width/18
        )
        self.color_picker_btn.grid(row=0, column=0, sticky="NS", pady=(15, 15))

        # robots_container = ttk.Frame(self, width=19*self.width/20, height=self.height)
        # robots_container.grid(row=0, column=1, padx=(10,10), pady=(15,15), sticky="NSWE")
        # robots_container["style"] = "BackgroundRED.TFrame"
        robot1 = Robot(self, height=height, width=width)
        robot1.grid(row=0, column=1, padx=(20, 20), pady=(15, 15), sticky="NSEW")#, sticky="NSEW", padx=(10, 0), pady=(10, 0))

        robot2 = Robot(self, height=height, width=width)
        robot2.grid(row=0, column=2, padx=(20, 20), pady=(15, 15), sticky="NSEW")#, sticky="NSEW", padx=(10, 0), pady=(10, 0))

        robot3 = Robot(self, height=height, width=width)
        robot3.grid(row=0, column=3, padx=(20, 20), pady=(15, 15), sticky="NSEW")#, sticky="NSEW", padx=(10, 0), pady=(10, 0))
    