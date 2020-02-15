from tkinter import *
import time
import os
import socket

import config

def sendInstruction(instruction, socket_list):
    """
    instruction: string with instruction, full documentation is in notion
    destinations: list with tuples (ip, port)
    """
    for sock in socket_list:
        sock.send(b"234234")
        print(f"sent {instruction} to {sock.getpeername()}.")
        

class App(Frame):
    def __init__(self,master, write_sockets, read_socket):
        """
        write_sockets: list of 3 sockets already connected to the robots
        """
        Frame.__init__(self, master)
        self.count = 0
        self.master = master

        self.dato_0 = Label(master, text="234", fg="Black", font=("Helvetica", 30))
        self.dato_0.grid(column=0)
        self.instrucciones_0 = []
        self.instrucciones_0.append(Button(master, text="Turn off", command=lambda: sendInstruction("0", [write_sockets[0]]), font=('Helvetica', 16)))
        self.instrucciones_0.append(Button(master, text="Turn on", command=lambda: sendInstruction("1", [write_sockets[0]]), font=('Helvetica', 16)))
        for i in self.instrucciones_0:
            i.grid(column=0)

        self.dato_1 = Label(master, text="sup", fg="Black", font=("Helvetica", 30))
        self.dato_1.grid(column=1)
        self.boton_1_1 = Button(master, text="Turn off", command=lambda: sendInstruction("0", [write_sockets[1]]), font=('Helvetica', 16))
        self.boton_1_1.grid(column=1)

        self.dato_3 = Label(master, text="sup", fg="Black", font=("Helvetica", 30))
        self.dato_3.grid(column=2)
        self.boton_3_1 = Button(master, text="Turn off", command=lambda: sendInstruction("0", [write_sockets[2]]), font=('Helvetica', 16))
        self.boton_3_1.grid(column=2)

        self.title_3 = Label(master, text="All", fg="red", font=("Helvetica", 30))
        self.title_3.grid(column=3)
        self.boton_3 = Button(master, text="Turn off", command=lambda: sendInstruction("0", write_sockets), font=('Helvetica', 16))
        self.boton_3.grid(column=3)

        self.update_data()

    def update_data(self):
        self.dato_0.configure(text=str(self.count))
        self.count+=1
        self.after(1000, self.update_data)


if __name__ == '__main__':

    # Server configuration

    read_socket = socket.socket()
    # write_sockets is the list of sockets used to send data, they are passed as parameters to the gui
    write_sockets = [socket.socket(), socket.socket(), socket.socket()]

    # Code for getting local IP
    local_ip = [l for l in ([ip for ip in socket.gethostbyname_ex(socket.gethostname())[2] 
        if not ip.startswith("127.")][:1], [[(s.connect(('8.8.8.8', 53)), 
        s.getsockname()[0], s.close()) for s in [socket.socket(socket.AF_INET, 
        socket.SOCK_DGRAM)]][0][1]]) if l][0][0]
    
    # Ask if you want to use data from config.py instead of writing it everytime you test
    opc = input("Do you want to load configurations from 'config.py'? (y/n): ")

    port = 4000
    # Grabs data from config.py
    if(opc.lower() == 'y'):
        port = config.sockets['LOCAL_PORT']
        read_socket.bind(('0.0.0.0', port))
        for i in range(3):
            try:
                write_sockets[i].connect((config.sockets['ROBOTS'][i][0], config.sockets['ROBOTS'][i][1]))
            except:
                print("Error: Robots are not connected yet.")
                exit()
            print(f"IP - {i}: {config.sockets['ROBOTS'][i][0]}")
            print(f"PORT - {i}: {config.sockets['ROBOTS'][i][1]}")
    # Manual data entry
    else:
        port = int(input("PORT to listen: "))
        read_socket.bind(('0.0.0.0',  port))
        for i in range(3):
            ip = input(f"IP - {i}: ")
            port = int(input(f"PORT - {i}: "))
            write_sockets[i].connect((ip,port))

    print(f"## Server running on {local_ip}:{port} ##")

    # Run of the main loop after configuration
    app=App(Tk(), write_sockets, read_socket)
    mainloop()