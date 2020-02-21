import tkinter as tk
from tkinter import ttk

class Ball(ttk.Frame):
    def __init__(self, parent, height, width):
        super().__init__(parent)

        self["height"] = height/3
        self["width"] = width=width/3
        self["style"] = "BackgroundWHITE.TFrame"