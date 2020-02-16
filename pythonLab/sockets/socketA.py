import socket
import time
import random

x = 5000
y = 400

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s1:
    s1.connect(('192.168.1.71', 9000))
    while True:
        try:
            data = f'|{x},{y}.'
            print(data)
            s1.send(data.encode("utf-8"))
            time.sleep(.02)
            x += random.randint(-2, 2)
            y += random.randint(-2, 2)
        except:
            s1.close()
