import tkinter as tk
from tkinter import ttk

def range_selector(color_code):
    root = tk.Tk()
    root.title('Range Selector')
    root.geometry('400x300')

    root.columnconfigure(1, weight=1)
    root.rowconfigure(0, weight=1)
    root.rowconfigure(1, weight=1)
    root.rowconfigure(2, weight=1)

    channel_1_value = tk.IntVar()
    channel_2_value = tk.IntVar()
    channel_3_value = tk.IntVar()

    def set_value1(event):
        channel_1_value.set(int(channel_1_scale.get()))

    def set_value2(event):
        channel_2_value.set(int(channel_2_scale.get()))

    def set_value3(event):
        channel_3_value.set(int(channel_3_scale.get()))

    channel_1_scale = ttk.Scale(root,
                               orient='horizontal',
                               from_=0,
                               to=255,
                               command=set_value1)

    channel_2_scale = ttk.Scale(root,
                               orient='horizontal',
                               from_=0,
                               to=255,
                               command=set_value2)

    channel_3_scale = ttk.Scale(root,
                               orient='horizontal',
                               from_=0,
                               to=255,
                               command=set_value3)


    if color_code == 'h':
        channel_1_label = ttk.Label(root, text='H:', padding=10)
        channel_2_label = ttk.Label(root, text='S:', padding=10)
        channel_3_label = ttk.Label(root, text='V:', padding=10)

    elif color_code == 'r':
        channel_1_label = ttk.Label(root, text='R:', padding=10)
        channel_2_label = ttk.Label(root, text='G:', padding=10)
        channel_3_label = ttk.Label(root, text='B:', padding=10)

    elif color_code == 'l':
        channel_1_label = ttk.Label(root, text='L:', padding=10)
        channel_2_label = ttk.Label(root, text='A:', padding=10)
        channel_3_label = ttk.Label(root, text='B:', padding=10)

    channel_1_selection = ttk.Label(root, textvariable=channel_1_value, padding=10)
    channel_2_selection = ttk.Label(root, textvariable=channel_2_value, padding=10)
    channel_3_selection = ttk.Label(root, textvariable=channel_3_value, padding=10)

    done_button = ttk.Button(root, text='Done', command=root.destroy)

    channel_1_label.grid(row=0, column=0)
    channel_2_label.grid(row=1, column=0)
    channel_3_label.grid(row=2, column=0)

    channel_1_scale.grid(row=0, column=1, sticky='EW')
    channel_2_scale.grid(row=1, column=1, sticky='EW')
    channel_3_scale.grid(row=2, column=1, sticky='EW')

    channel_1_selection.grid(row=0, column=2)
    channel_2_selection.grid(row=1, column=2)
    channel_3_selection.grid(row=2, column=2)

    done_button.grid(row=3, column=1, pady=15, sticky='EW')

    root.mainloop()
    return channel_1_value.get(), channel_2_value.get(), channel_3_value.get()

if __name__ == "__main__":
    range_selector()