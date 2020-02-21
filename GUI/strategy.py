import tkinter as tk
from tkinter import ttk

class Strategy(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self["height"] = height
        self["width"] = width=width/2
        self["style"] = "BackgroundPURPLE.TFrame"