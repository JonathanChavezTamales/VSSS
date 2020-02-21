import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Robot(ttk.Frame):
        def __init__(self, parent, height, width, player_mode):
            super().__init__(parent)

            self.height = .85*height/3
            self.width = .9*width/3

            self["height"] = self.height
            self["width"] = self.width
            self["style"] = "Background.TFrame"

            self.parent = parent

            BACKGROUND_PATH = "Assets/robot_frame.jpg"
            background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(1*self.width), int(1*self.height)), Image.ANTIALIAS))
            background_label = tk.Label(self, image=background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_image

            self.x = tk.StringVar(value="morado gei")
            self.y = tk.StringVar(value="0")
            self.vision_angle = tk.StringVar(value="0")
            self.giroscope_angle = tk.StringVar(value="0")
            self.icon = player_mode

            ICON_PATH = "Assets/robot_frame.jpg"
         
           # background_label.place(x=0, y=0, relwidth=1, relheight=1)

            self.columnconfigure(1, weight=1)
            self.columnconfigure(2, weight=1)
            self.grid_propagate(0) #disables grid shrinking

            icon_image = ImageTk.PhotoImage(Image.open(ICON_PATH).resize((int(.2*self.width), int(.3*self.height)), Image.ANTIALIAS))
            self.label_icon = tk.Label(self, image=icon_image)
            self.label_icon.grid(column=0, row=0, sticky="NSEW", padx=(30,10), pady=(85,60), rowspan=3)
            self.label_icon.image = background_image

            label_x = ttk.Label(
                self, 
                textvariable=self.x
            )
            label_x.grid(column=1, row=0, sticky="NSEW", padx=(30,10), pady=(60,10))

            label_y = ttk.Label(
                self, 
                textvariable=self.y
            )
            label_y.grid(column=2, row=0, sticky="NSEW", padx=(20,10), pady=(60,10))

            label_vision_angle = ttk.Label(
                self,
                textvariable=self.vision_angle
            )
            label_vision_angle.grid(column=1, row=1, sticky="NSEW", padx=(30,10), pady=(10,10), columnspan=2)

            label_giroscope_angle = ttk.Label(
                self, 
                textvariable=self.giroscope_angle
            )
            label_giroscope_angle.grid(column=1, row=2, sticky="NSEW", padx=(30,10), pady=(10,60), columnspan=2)

            self.color_picker_btn = ttk.Button(
                self,
                text="",
                #command=,
                cursor="hand2",
                width=self.width/8
            )
            self.color_picker_btn.grid(row=0, column=3, sticky="NS", pady=(80, 80), padx=(15,15), rowspan=3)

        
 

            


            
        
