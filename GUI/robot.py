import tkinter as tk
from tkinter import ttk

class Robot(ttk.Frame):
        def __init__(self, parent, height, width):
            super().__init__(parent)

            self["padding"] = (20, 20, 20, 20)
            self["height"] = height/3-40
            self["width"] = width=width/3-40
            self["style"] = style="BackgroundPINK.TFrame"