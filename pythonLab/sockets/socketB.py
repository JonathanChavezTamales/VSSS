import socket
import time

def send_data(s):
    for i in range(1000, 2000):
        s.send(b'1000')
        time.sleep(1)


s1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s1.connect(('192.168.1.71', 3500))

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s2:
    s2.bind(('192.168.1.71', 9000))
    s2.listen(5)

    client, addr = s2.accept()
    print("new conn: ", addr)
    
    while True:
        data = client.recv(100)
        if data:
            print(data)
            s1.send(data)
        else:
            break


#send_data(s1)


