import tkinter as tk
from tkinter import ttk

class Robot(ttk.Frame):
        def __init__(self, parent, height, width):
            super().__init__(parent)

            self.height = .89*height/3
            self.width = .89*width/3

            self["height"] = self.height
            self["width"] = self.width
            self["style"] = "BackgroundPINK.TFrame"
        
