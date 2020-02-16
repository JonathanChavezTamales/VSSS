from object_pb2 import ObjectData

x = ObjectData()
x.kind = 2
x.id = 1
x.x = 3432
x.y = 2349

y = ObjectData()
y.kind = 1
y.id = 1
y.x = 1900
y.y = 3498
y.yaw = 98

print(x)
print(x.SerializeToString())
print(y)
print(y.SerializeToString())

import socket
s = socket.socket()
s.connect(('10.43.63.47', 4000))
s.sendall(y.SerializeToString())