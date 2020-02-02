import os
import socket

lastData = ""
currentBuffer = ""

def main():
    s = socket.socket()

    s.bind(('0.0.0.0', 4000 ))
    s.listen(0) 

    ssend = socket.socket()
    ssend.connect(('192.168.0.103', 80))
              

    while True:
        client, addr = s.accept()
        

        while True:
            content = client.recv(45)
            
            if len(content) ==0:
                break

            else:
                parse(content.decode("utf-8"))
                print(lastData)
                ssend.send(lastData.encode())
                #coords = stream_to_coordinates(lastData)
                #print(coords)
                #print_coordinates(coords)
                   
        client.close()

    ssend.close()

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

main()
