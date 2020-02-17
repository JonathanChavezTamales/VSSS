from tkinter import ttk
import tkinter as tk


class Main(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


        SCREEN_WIDTH = self.winfo_screenwidth()
        SCREEN_HEIGHT = self.winfo_screenheight()

        self.title('ALPHA SOCCER FC v1.0')
        self.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.resizable(False, False)

        print(SCREEN_HEIGHT, SCREEN_WIDTH)
        


root = Main()
root.mainloop()