from object_pb2 import ObjectData
import socket
import time
from random import randint

s = socket.socket()
s.connect(('192.168.0.100', 4000))

while True:
    print("sending")
    y = ObjectData()
    y.kind = 1
    y.id = randint(0,2)
    y.team = 1
    y.x = randint(0,1000)
    y.y = randint(0,1000)
    y.yaw = randint(0,361)
    print(y.SerializeToString())
    s.sendall(y.SerializeToString())
    time.sleep(.1)