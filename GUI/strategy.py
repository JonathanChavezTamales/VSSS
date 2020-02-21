import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Strategy(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self.height = int(height)
        self.width = int(width)

        self["height"] = self.height
        self["width"] =  self.width
        self["style"] = "BackgroundPURPLE.TFrame"

        BACKGROUND_PATH = "Assets/f3.jpg"
        background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        background_label = tk.Label(self, image=background_image)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = background_image