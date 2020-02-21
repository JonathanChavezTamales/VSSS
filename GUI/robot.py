import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Robot(ttk.Frame):
        def __init__(self, parent, height, width):
            super().__init__(parent)

            self.height = .85*height/3
            self.width = .9*width/3

            self["height"] = self.height
            self["width"] = self.width
            self["style"] = "Background.TFrame"

            BACKGROUND_PATH = "Assets/r1.jpg"
            background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(1*self.width), int(1*self.height)), Image.ANTIALIAS))
            background_label = tk.Label(self, image=background_image)
            background_label.place(x=0, y=0, relwidth=1, relheight=1)
            background_label.image = background_image
        
