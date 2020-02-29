import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Info_Panel(ttk.Frame):
    def __init__(self, container, robot, show_main_panel):
        super().__init__(container)

        self.robot = robot

        self.height = self.robot.height
        self.width = self.robot.width

        self["height"] = self.height
        self["width"] = self.width
        self["style"] = "Background.TFrame"

        background_label = tk.Label(self, image=self.robot.BACKGROUND_IMAGE)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)
        background_label.image = self.robot.BACKGROUND_IMAGE


        print('alias', self.robot.ip_address.get())

        self.grid_propagate(0) #disables grid shrinking

        label_alias_tag = ttk.Label(
            self, 
            text="Alias: ",
            style="LightText.TLabel"
        )
        label_alias_tag.grid(column=0, row=0, sticky="EW", padx=(30,30), pady=(10,10))

        label_alias = ttk.Label(
            self, 
            textvariable=self.robot.alias,
            style="LightText.TLabel"
        )
        label_alias.grid(column=1, row=0, sticky="EW", padx=(30,30), pady=(10,10))

        label_ip_address_tag = ttk.Label(
            self, 
            text="IP: ",
            style="LightText.TLabel"
        )
        label_ip_address_tag.grid(column=0, row=1, sticky="EW", padx=(30,30), pady=(10,10))

        label_ip_address = ttk.Label(
            self, 
            textvariable=self.robot.ip_address,
            style="LightText.TLabel"
        )
        label_ip_address.grid(column=1, row=1, sticky="EW", padx=(30,30), pady=(10,10))

        label_mac_address_tag = ttk.Label(
            self, 
            text="MAC: ",
            style="LightText.TLabel"
        )
        label_mac_address_tag.grid(column=0, row=2, sticky="EW", padx=(30,30), pady=(10,10))

        label_mac_address = ttk.Label(
            self, 
            textvariable=self.robot.mac_address,
            style="LightText.TLabel"
        )
        label_mac_address.grid(column=1, row=2, sticky="EW", padx=(30,30), pady=(10,10))

        label_server_port_tag = ttk.Label(
            self, 
            text="Server Port: ",
            style="LightText.TLabel"
        )
        label_server_port_tag.grid(column=0, row=3, sticky="EW", padx=(10,10), pady=(10,10))

        label_server_port = ttk.Label(
            self, 
            textvariable=self.robot.server_port,
            style="LightText.TLabel"
        )
        label_ip_address.grid(column=1, row=3, sticky="EW", padx=(10,10), pady=(10,10))

        label_client_port_tag = ttk.Label(
            self, 
            text="Client Port: ",
            style="LightText.TLabel"
        )
        label_server_port_tag.grid(column=0, row=4, sticky="EW", padx=(30,30), pady=(10,10))

        label_client_port = ttk.Label(
            self, 
            textvariable=self.robot.client_port,
            style="LightText.TLabel"
        )
        label_ip_address.grid(column=1, row=4, sticky="EW", padx=(30,30), pady=(10,10))