from tkinter import *
import time
import os
import socket
from threading import Thread
from multiprocessing import Process, Queue

import config
from game import State, Robot, Ball
from object_pb2 import ObjectData




class App(Frame):
    def __init__(self,master, write_sockets, read_socket):
        """
        write_sockets: list of 3 sockets already connected to the robots
        """
        Frame.__init__(self, master)
        # game_state contains all the real time information about the game
        self.game_state = State(
            home_robots=[Robot(rid=0, team=1, color="blue", sock=write_sockets[0]), Robot(rid=1, team=1, color="red", sock=write_sockets[1]), Robot(rid=2, team=1, color="pink", sock=write_sockets[2])],
            away_robots=[Robot(rid=0, team=2), Robot(rid=1, team=2), Robot(rid=2, team=2)],
            ball=Ball()
            )
        self.master = master
        self.read_socket = read_socket

        # Threads for listening data and updating ui
        # self.listener = Thread(target=self.listen_data)
        # self.listener.start()

        self.dato_0 = Label(master, text="1", fg="Black", font=("Helvetica", 30), padx=100)
        self.dato_0.grid(column=0)
        self.instrucciones_0 = []
        self.instrucciones_0.append(Button(master, text="Turn off", command=lambda: self.sendInstruction("0", [self.game_state.home_robots[0].socket]), font=('Helvetica', 16)))
        self.instrucciones_0.append(Button(master, text="Turn on", command=lambda: self.sendInstruction("1", [self.game_state.home_robots[0].socket]), font=('Helvetica', 16)))
        for i in self.instrucciones_0:
            i.grid(column=0)

        self.dato_1 = Label(master, text="1", fg="Black", font=("Helvetica", 30), padx=100)
        self.dato_1.grid(column=1)
        self.instrucciones_1 = []
        self.instrucciones_1.append(Button(master, text="Turn off", command=lambda: self.sendInstruction("0", [self.game_state.home_robots[1].socket]), font=('Helvetica', 16)))
        self.instrucciones_1.append(Button(master, text="Turn on", command=lambda: self.sendInstruction("1", [self.game_state.home_robots[1].socket]), font=('Helvetica', 16)))
        for i in self.instrucciones_1:
            i.grid(column=1)

        self.dato_2 = Label(master, text="2", fg="Black", font=("Helvetica", 30), padx=100)
        self.dato_2.grid(column=2)
        self.instrucciones_2 = []
        self.instrucciones_2.append(Button(master, text="Turn off", command=lambda: self.sendInstruction("0", [self.game_state.home_robots[2].socket]), font=('Helvetica', 16)))
        self.instrucciones_2.append(Button(master, text="Turn on", command=lambda: self.sendInstruction("1", [self.game_state.home_robots[2].socket]), font=('Helvetica', 16)))
        for i in self.instrucciones_2:
            i.grid(column=2)

        # Sends to all robots
        self.dato_3 = Label(master, text="ALL", fg="red", font=("Helvetica", 30, "bold"), padx=100)
        self.dato_3.grid(column=3)
        self.instrucciones_3 = []
        self.instrucciones_3.append(Button(master, text="Turn off", command=lambda: self.sendInstruction("0", [robot.socket for robot in self.game_state.home_robots]), font=('Helvetica', 16)))
        self.instrucciones_3.append(Button(master, text="Turn on", command=lambda: self.sendInstruction("1", [robot.socket for robot in self.game_state.home_robots]), font=('Helvetica', 16)))
        for i in self.instrucciones_3:
            i.grid(column=3)

        # Match details
        score = f"{self.game_state.home_goals} - {self.game_state.away_goals}"
        self.score = Label(master, text=score, fg="green", font=("Helvetica", 40, "bold"), padx=150)
        self.score.grid(column=4)

        
        self.update_data()

    def listen(self):
        self.read_socket.listen(0)
        while True:
            client, addr = self.read_socket.accept()
            while True:
                content = client.recv(45) # Serialized protobuff data
                if len(content) ==0:
                    break
                else:
                    self.game_state.update(content)
                    print("new message")
            client.close()
        

    def sendInstruction(self, instruction, sockets):
        """
        instruction: string with instruction, full documentation is in notion.
        destinations: list with tuples (ip, port)
        """
        for sock in sockets:
            sock.send(instruction.encode("utf-8"))
            print(f"sent {instruction} to {sock.getpeername()}.")

    def update_data(self):
        """
            Updates GUI in real time based on data received by the sockets.
            1.- Reads from ground and vision sockets
            2.- Parses the data
            3.- Updates self.game_state
        """
        # TODO: (total sockets) - Benchmark  read_socket (1) vs one socket for each reading (3)
        
        self.dato_0.configure(text=self.game_state.home_robots[0].x)
        self.dato_1.configure(text=self.game_state.home_robots[1].x)
        self.dato_2.configure(text=self.game_state.home_robots[2].x)

        score = f"{self.game_state.home_goals} - {self.game_state.away_goals}"
        self.score.configure(text=score)
        self.after(50, self.update_data)


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

    port = int(input("PORT to listen: "))
    print(f"## Server will run on {local_ip}:{port} ##")

    
    # Ask if you want to use data from config.py instead of writing it everytime you test
    opc = input("Do you want to load configurations from 'config.py'? (y/n): ")

    port = 4000
    # Grabs data from config.py
    if(opc.lower() == 'y'):
        port = config.sockets['LOCAL_PORT']
        read_socket.bind(('0.0.0.0', port))
        for i in range(3):
            try:
                pass
                #write_sockets[i].connect((config.sockets['ROBOTS'][i][0], config.sockets['ROBOTS'][i][1]))
            except:
                print("Error: Robots are not connected yet.")
                exit()
            print(f"IP - {i}: {config.sockets['ROBOTS'][i][0]}")
            print(f"PORT - {i}: {config.sockets['ROBOTS'][i][1]}")
            time.sleep(.3)
    # Manual data entry
    else:
        read_socket.bind(('0.0.0.0',  port))
        #read_socket.listen(0)
        for i in range(3):
            ip = input(f"IP - {i}: ")
            port = int(input(f"PORT - {i}: "))
            write_sockets[i].connect((ip,port))

    # One process for reading from socket, another for ui and writing
    
    app=App(Tk(), write_sockets, read_socket)

    p = Thread(target=app.listen)
    p.start()
    app.mainloop()
    p.join()