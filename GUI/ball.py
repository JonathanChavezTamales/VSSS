import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Ball(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "BackgroundORANGE.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)


        self.x = tk.StringVar(value="morado gei")
        self.y = tk.StringVar(value="0")
    

        BACKGROUND_PATH = "Assets/panel_background.jpg"
        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image


        ICON_PATH = "Assets/robot_frame.jpg"
        icon_image = ImageTk.PhotoImage(Image.open(ICON_PATH).resize((int(.2*self.width), int(.3*self.height)), Image.ANTIALIAS))
        self.label_icon = tk.Label(self, image=icon_image)
        self.label_icon.grid(column=0, row=0, sticky="NSEW", padx=(30,10), pady=(85,60), rowspan=3)
        self.label_icon.image = background_image
    