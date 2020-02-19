import tkinter as tk
from tkinter import ttk


class Settings(ttk.Frame):
    def __init__(self, parent, controller, show_timer, height, width):
        super().__init__(parent)

        self["style"] = "BackgroundRED.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        settings_container = ttk.Frame(
            self,
            padding="30 15 30 15",
            style="BackgroundRED.TFrame"
        )

        settings_container.grid(row=0, column=0, sticky="NSEW", padx=10, pady=10)

        settings_container.columnconfigure(0, weight=1)
        settings_container.rowconfigure(0, weight=1)


        for child in settings_container.winfo_children():
            child.grid_configure(padx=5, pady=5)


        timer_button = ttk.Button(
            settings_container,
            text="← Back",
            command=show_timer,
            style="Button.TButton",
            cursor="hand2"  # hand1 in some systems
        )

        timer_button.grid(column=0, row=0, sticky="NSEW", padx=2)
