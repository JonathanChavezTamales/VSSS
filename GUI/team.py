import tkinter as tk
from tkinter import ttk
from robot import Robot
from PIL import ImageTk,Image


class Team(ttk.Frame):
    def __init__(self, parent, height, width, is_enemy_team, color):
        super().__init__(parent)

        self.height = int(height/3)
        self.width = int(width)

        self["height"] = self.height
        self["width"] = self.width

        self.parent = parent

        self.color = color

        print(self.color)


        # self.columnconfigure(1, weight=1)
        # self.rowconfigure(0, weight=1)
    
        BACKGROUND_PATH = "Assets/team1_background.jpg" if not is_enemy_team else "Assets/team2_background.jpg"
        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((self.width, self.height), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image

        # self.color_picker_btn = ttk.Button(
        #     self,
        #     text="",
        #     #command=self.start_timer,
        #     cursor="hand2",
        #     width=self.width/18
        # )
        # self.color_picker_btn.grid(row=0, column=0, sticky="NS", pady=(15, 15))

        self.color_bar = tk.Label(self, bg=self.color)
        self.color_bar.grid(row=0, column=0, sticky="NS", pady=(15,15))

        self.robot1 = Robot(self, height=height, width=width, player_mode="goalkeeper", is_enemy=is_enemy_team, color="green")
        self.robot1.grid(row=0, column=1, padx=(20, 20), pady=(15, 15), sticky="NSEW")#, sticky="NSEW", padx=(10, 0), pady=(10, 0))

        self.robot2 = Robot(self, height=height, width=width, player_mode="jugador", is_enemy=is_enemy_team, color="pink")
        self.robot2.grid(row=0, column=2, padx=(20, 20), pady=(15, 15), sticky="NSEW")#, sticky="NSEW", padx=(10, 0), pady=(10, 0))

        self.robot3 = Robot(self, height=height, width=width, player_mode="jugador", is_enemy=is_enemy_team, color="yellow")
        self.robot3.grid(row=0, column=3, padx=(20, 20), pady=(15, 15), sticky="NSEW")#, sticky="NSEW", padx=(10, 0), pady=(10, 0))

    
    