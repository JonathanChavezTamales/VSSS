# Reads from two sockets in different processes
import os
import socket
import time
from multiprocessing import Process, Value

lastData = ""
currentBuffer = ""

def main(num, port_listen, ip_send, port_send):
    print(f"main de {ip_send}")
    socket_read = socket.socket()
    socket_send = socket.socket()
    shared_val = Value('i', 0)
    p_read = Process(target=read, args=(num, socket_read, shared_val,))
    p_write = Process(target=write, args=(socket_send, shared_val, ))

    # Reader
    socket_read.bind(('0.0.0.0', port_listen ))
    socket_read.listen(0)

    # Sender
    socket_send.connect((ip_send, port_send))
              
    # Process startup
    p_read.start()
    p_write.start()

    print(f"PID1: {p_read.pid}")
    print(f"PID2: {p_write.pid}")
    

    socket_send.close()
    socket_read.close()


def write(s, val):
    time.sleep(.1)
    print(val.value)
    s.send(b"300")


def read(num, s, val):
    print("reader")
    while True:
        client, addr = s.accept()
        
        while True:
            content = client.recv(45)
            
            if len(content) ==0:
                break

            else:
                parse(content.decode("utf-8"))
                print(f"Data {num}:", lastData)
                print(lastData)
                newval = int(lastData)
                val.value =  4#int(lastData)
                #s.send(lastData.encode()) 
                #coords = stream_to_coordinates(lastData)
                #print(coords)
                #print_coordinates(coords)    
        client.close()



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
agus = Process(target=main, args=("ags", 4001,'192.168.0.18', 1018))
jpr = Process(target=main, args=("jpr", 4000, '192.168.0.101', 4100))

#agus.start()
jpr.start()
print(f"start {agus.pid} y {jpr.pid}")
#agus.join()
jpr.join()
