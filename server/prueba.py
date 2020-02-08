# Reads from two sockets in different processes
import os
import socket
from multiprocessing import Process, Value

lastData = ""
currentBuffer = ""

def main(port_listen, ip_send, port_send):
    print(f"main de {ip_send}")
    socket_read = socket.socket()
    socket_send = socket.socket()
    shared_val = Value('i', 0)
    p_read = Process(target=read, args=(socket_read,socket_send, shared_val,))

    # Reader
    socket_read.bind(('0.0.0.0', port_listen ))
    socket_read.listen(0)

    # Sender
    socket_send.connect((ip_send, port_send))
              
    # Process startup
    p_read.start()
    print(f"PID1: {p_read.pid}")
    

    socket_send.close()
    socket_read.close()

def read(s,ssender, val):
    print("reader")
    while True:
        client, addr = s.accept()
        
        while True:
            content = client.recv(45)
            
            if len(content) ==0:
                break

            else:
                parse(content.decode("utf-8"))
                print(lastData)
                #val.value += 1
                #s.send(lastData.encode())
                #p = Process(target=send, args=(ssender, val))
                #p.start()
                #print(f"PID2: {p.pid}")
                #p.join()
                #coords = stream_to_coordinates(lastData)
                #print(coords)
                #print_coordinates(coords)    
        client.close()

def send(s, val):
    string = f"300"
    s.send(string.encode())


def parse(s):
    """receives a tcp packet from the socket and formats it"""
    global lastData
    global currentBuffer
    

    currentBuffer += s
    pos = currentBuffer.find(".")
    

    if pos != -1:
        lastData = currentBuffer[1:pos]
        currentBuffer = currentBuffer[pos+1:]


def stream_to_coordinates(stream):
    coords = (0,0,0)
    if len(lastData) > 1:
        coords = tuple(map(int, lastData[1:-1].split(",")))
    return coords

def print_coordinates(position):
    os.system('cls')
    for i in range(50):
        for j in range(150):
            if position[0] == i and position[1] == j:
                print("🐌", end="")
            else:
                print(".", end="")
        print()

# Main processes
agus = Process(target=main, args=(4001,'192.168.0.18', 1018))
jpr = Process(target=main, args=(4000, '192.168.0.101', 4100))

agus.start()
jpr.start()
print(f"start {agus.pid} y {jpr.pid}")
agus.join()
agus.join()
