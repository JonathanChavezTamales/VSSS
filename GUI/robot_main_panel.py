import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Main_Panel(ttk.Frame):
    def __init__(self, container, robot, show_info_panel):
        super().__init__(container)

        self.robot = robot

        self.height = self.robot.height
        self.width = self.robot.width

        self["height"] = self.height
        self["width"] = self.width
        
        self["style"] = "Background.TFrame"

        background_label = tk.Label(self, image=self.robot.BACKGROUND_IMAGE)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = self.robot.BACKGROUND_IMAGE

        self.grid_propagate(0) #disables grid shrinking

        ICON_PATH = "Assets/goalkeeper.png" if self.robot.player_mode == 'goalkeeper' else "Assets/soccer_player.png"
        icon_image = ImageTk.PhotoImage(Image.open(ICON_PATH).resize((int(.2*self.width), int(.3*self.height)), Image.ANTIALIAS))
        self.label_icon = tk.Label(self, image=icon_image, borderwidth=0, highlightthickness=0, padx=0,pady=0)
        self.label_icon.grid(column=0, row=0, sticky="NSEW", padx=(20,20), pady=(85,60), rowspan=3)
        self.label_icon.image = icon_image

        label_x = ttk.Label(
            self, 
            textvariable=self.robot.x,
            style="LightText.TLabel"
        )
        label_x.grid(column=1, row=0, sticky="EW", padx=(30,50), pady=(60,10))

        label_y = ttk.Label(
            self, 
            textvariable=self.robot.y,
            style="LightText.TLabel"
        )
        label_y.grid(column=2, row=0, sticky="EW", padx=(30,50), pady=(60,10))

        label_vision_angle = ttk.Label(
            self,
            textvariable=self.robot.vision_angle,
            style="LightText.TLabel"
        )
        label_vision_angle.grid(column=1, row=1, sticky="EW", padx=(30,10), pady=(10,10))

        
        label_giroscope_angle = ttk.Label(
            self, 
            textvariable=self.robot.giroscope_angle,
            style="LightText.TLabel"
        )
        label_giroscope_angle.grid(column=1, row=2, sticky="EW", padx=(30,30), pady=(10,60))

        self.color_bar = tk.Label(self, bg=self.robot.color)
        self.color_bar.grid(row=0, column=2, sticky="NS", pady=(80, 0), padx=(180,15), rowspan=2, columnspan=2)

        I_ICON_PATH = "Assets/i_icon.png"
        i_icon_image = ImageTk.PhotoImage(Image.open(I_ICON_PATH).resize((int(.07*self.width), int(.125*self.height)), Image.ANTIALIAS))
        info_button = tk.Button(
            self, 
            image=i_icon_image, 
            borderwidth=0, 
            highlightthickness=0, 
            padx=0,
            pady=0,
            cursor="hand2",
            command=show_info_panel
        )
        info_button.grid(row=2, column=1, columnspan=4, pady=(10, 0), padx=(int(self.width*.62),0))
        info_button.image = i_icon_image
