import tkinter as tk
from tkinter import ttk
from team import Team
from ball import Ball
from strategy import Strategy
from PIL import Image, ImageTk


class Dashboard(ttk.Frame):
    def __init__(self, parent, controller, show_settings, height, width):
        super().__init__(parent)

        self["style"] = "Background.TFrame"
        self["height"] = height
        self["width"] = width

        self.parent = parent

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        INITIAL_CONFIGURATION_FILE_PATH = "Configuration/initial_configuration.csv"

        initial_configuration_file = open(INITIAL_CONFIGURATION_FILE_PATH, "r")

        teams = {"team1":[], "team2":[]}

        lines = initial_configuration_file.readlines()
        DATA_HEADERS = lines[0].split(",")
        for line in lines[1:]:
            data = line.split(",")
            robot_data = {DATA_HEADERS[x].replace(" ", "").replace("\n", "") : data[x].replace(" ", "").replace("\n", "") for x in range(len(data))}
            print(robot_data.keys())
            teams[robot_data["team_number"]].append(robot_data)

        initial_configuration_file.close()
             
        self.team1 = Team(self, height=height, width=width, initial_data=teams["team1"])
        self.team1.grid(row=0, column=0, sticky="NSEW", columnspan=3, pady=(0, 15))

        self.team2 = Team(self, height=height, width=width, initial_data=teams["team2"])
        self.team2.grid(row=1, column=0, sticky="NSEW", columnspan=3, pady=(0, 15))

        self.control_panel = ttk.Frame(self, height=height/3, width=width, style = "BackgroundORANGE.TFrame")
        self.control_panel.grid(row=2, column=0, sticky="NSEW", columnspan=3)

        self.ball = Ball(self, height=height/3, width=width/3)
        self.ball.grid(row=2, column=0, sticky="NSEW")

        self.strategy = Strategy(self, height=height/3, width=2*width/3)
        self.strategy.grid(row=2, column=1, sticky="NSEW")

        # ajustes = ttk.Frame(self, height=height/3, width=width/6, style="BackgroundRED.TFrame")
        # ajustes.grid(row=2, column=2, sticky="NSEW")

        # settings_button = ttk.Button(
        #     ajustes,
        #     style = "Button.TButton",
        #     text="Settings",
        #     command=show_settings,
        #     cursor="hand2"
        # )
        # settings_button.grid(row=0, column=0, sticky="E", padx=10, pady=(10, 0))

      


  


      


    
   