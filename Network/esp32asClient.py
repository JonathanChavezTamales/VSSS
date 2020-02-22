import os
import socket


send = socket.socket()
send.connect(('192.168.0.103', 80))
            
os.system(ls)

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
