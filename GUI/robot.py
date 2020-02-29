import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from robot_main_panel import Main_Panel
from robot_info_panel import Info_Panel

class Robot(ttk.Frame):
    def __init__(self, parent, height, width, initial_data):
        super().__init__(parent)

        self.parent = parent

        self.height = .85*height/3
        self.width = .9*width/3

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.grid_propagate(0) #disables grid shrinking

        BACKGROUND_PATH = "Assets/robot_frame.jpg"
        self.BACKGROUND_IMAGE = ImageTk.PhotoImage(Image.open(BACKGROUND_PATH).resize((int(self.width), int(self.height)), Image.ANTIALIAS))
        
        print(initial_data)
        self.color = initial_data["robot_color"]
        self.x = tk.StringVar(value="x: 0")
        self.y = tk.StringVar(value="y: 0")
        self.vision_angle = tk.StringVar(value="0 º")
        self.giroscope_angle = tk.StringVar(value="0 º")
        self.player_mode = initial_data["player_mode"]
        print()
        self.alias = tk.StringVar(value=initial_data["alias"])
        self.ip_address = tk.StringVar(value=initial_data["ip_address"])
        self.mac_address = tk.StringVar(value=initial_data["mac_address"])
        self.server_port = tk.StringVar(value=initial_data["server_port"])
        self.client_port = tk.StringVar(value=initial_data["client_port"])

        print(f"""
                ALIAS: {self.alias.get()}
                IP: {self.ip_address.get()}
                MAC: {self.mac_address.get()}
                ServerPort: {self.server_port.get()}
                ClientePort: {self.client_port.get()}
            """)

        self.frames = {}

        container = ttk.Frame(self)
        container["height"] = self.height
        container["width"] = self.width
        container.grid()
        container.columnconfigure(0, weight=1)

        main_panel = Main_Panel(
                                container,
                                self, 
                                lambda: self.show_frame(Info_Panel), 
                            )

        info_panel = Info_Panel(
                                container, 
                                self, 
                                lambda: self.show_frame(Main_Panel), 
                            )

        main_panel.grid(row=0, column=0, sticky="NESW")
        info_panel.grid(row=0, column=0, sticky="NESW")

        self.frames[Main_Panel] = main_panel
        self.frames[Info_Panel] = info_panel
        
        self.show_frame(Main_Panel)
        
    def show_frame(self, container):
        frame = self.frames[container]
        frame.tkraise()

       



    


    


        


        
    
