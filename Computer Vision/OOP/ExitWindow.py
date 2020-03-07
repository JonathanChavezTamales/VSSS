import tkinter as tk
from tkinter import ttk

def exit_window():
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass

    root = tk.Tk()
    root.title('Quit')
    root.geometry('250x150')
    exit = tk.IntVar()

    def quit():
        exit.set(1)
        root.destroy()

    def cancel():
        exit.set(0)
        root.destroy()

    quit_label = ttk.Label(root, text='Are you sure you want to\nstop calibrating?', padding=20)
    quit_label.pack()

    buttons = ttk.Frame(root)
    buttons.pack()

    quit_button = ttk.Button(buttons, text='Quit', command=quit)
    quit_button.pack(side='left')

    cancel_button = ttk.Button(buttons, text='Cancel', command=cancel)
    cancel_button.pack(side='left')

    root.mainloop()
    return exit.get()


if __name__ == "__main__":
    exit_window()