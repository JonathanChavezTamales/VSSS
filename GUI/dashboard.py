import tkinter as tk
from tkinter import ttk
from team import Team
from ball import Ball
from strategy import Strategy


class Dashboard(ttk.Frame):
    def __init__(self, parent, controller, show_settings, height, width):
        super().__init__(parent)

        self["style"] = "BackgroundBLUE.TFrame"
        self["height"] = height
        self["width"] = width

        self.controller = controller
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        equipo1 = Team(self, height=height, width=width, isEnemyTeam=True)
        equipo1.grid(row=0, column=0, sticky="NSEW", columnspan=3)

        equipo2 = Team(self, height=height, width=width, isEnemyTeam=False)
        equipo2.grid(row=1, column=0, sticky="NSEW", columnspan=3)

        ball = Ball(self, height=height, width=width)
        ball.grid(row=2, column=0, sticky="NSEW")

        strategy = Strategy(self, height=height, width=width)
        strategy.grid(row=2, column=1, sticky="NSEW")

        ajustes = ttk.Frame(self, height=height/3, width=width/6, style="BackgroundRED.TFrame")
        ajustes.grid(row=2, column=2, sticky="NSEW")


        settings_button = ttk.Button(
            ajustes,
            style = "Button.TButton",
            text="Settings",
            command=show_settings,
            cursor="hand2"
        )
        settings_button.grid(row=0, column=0, sticky="E", padx=10, pady=(10, 0))

        # dashboard_frame = ttk.Frame(self, height="170", style="Dashboard.TFrame")
        # dashboard_frame.grid(row=1, column=0, columnspan=2, pady=(10, 0), sticky="NSEW")

   


  

      


    
   