import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Robot(ttk.Frame):
        def __init__(self, parent, height, width, player_mode, is_enemy, color):
            super().__init__(parent)

            self.height = .85*height/3
            self.width = .9*width/3

            self["height"] = self.height
            self["width"] = self.width
            self["style"] = "Background.TFrame"

            self.color = color

            self.parent = parent

            BACKGROUND_PATH = "Assets/robot_frame.jpg"
            background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(1*self.width), int(1*self.height)), Image.ANTIALIAS))
            background_label = tk.Label(self, image=background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_image

            self.x = tk.StringVar(value=f"x: 0")
            self.y = tk.StringVar(value="y: 0")
            self.vision_angle = tk.StringVar(value="0 º")
            self.giroscope_angle = tk.StringVar(value="0 º")
            self.icon = player_mode
         
           # background_label.place(x=0, y=0, relwidth=1, relheight=1)

            # self.columnconfigure(1, weight=1)
            # self.columnconfigure(2, weight=2)
            self.grid_propagate(0) #disables grid shrinking

            ICON_PATH = "Assets/goalkeeper.png" if player_mode == 'goalkeeper' else "Assets/soccer_player.png"
            icon_image = ImageTk.PhotoImage(Image.open(ICON_PATH).resize((int(.2*self.width), int(.3*self.height)), Image.ANTIALIAS))
            self.label_icon = tk.Label(self, image=icon_image, borderwidth=0, highlightthickness=0, padx=0,pady=0)
            self.label_icon.grid(column=0, row=0, sticky="NSEW", padx=(30,10), pady=(85,60), rowspan=3)
            self.label_icon.image = icon_image

            label_x = ttk.Label(
                self, 
                textvariable=self.x,
                style="LightText.TLabel"
            )
            label_x.grid(column=1, row=0, sticky="EW", padx=(30,50), pady=(60,10))

            label_y = ttk.Label(
                self, 
                textvariable=self.y,
                style="LightText.TLabel"
            )
            label_y.grid(column=2, row=0, sticky="EW", padx=(20,50), pady=(60,10))

            label_vision_angle = ttk.Label(
                self,
                textvariable=self.vision_angle,
                style="LightText.TLabel"
            )
            label_vision_angle.grid(column=1, row=1, sticky="EW", padx=(30,10), pady=(10,10))

            if not is_enemy:
                label_giroscope_angle = ttk.Label(
                    self, 
                    textvariable=self.giroscope_angle,
                    style="LightText.TLabel"
                )
                label_giroscope_angle.grid(column=1, row=2, sticky="EW", padx=(30,10), pady=(10,60))

            self.color_bar = tk.Label(self, bg=self.color)
            self.color_bar.grid(row=0, column=3, sticky="NS", pady=(80, 80), padx=(15,15), rowspan=3)

        
 

            


            
        
