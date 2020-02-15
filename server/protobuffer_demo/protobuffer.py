import robot_pb2
import sys

message = robot_pb2.RobotData()
message.id = 1
message.pitch = 40
message.roll = 345
message.battery = 11294

print(message)
serialized = message.SerializeToString()
print(sys.getsizeof(serialized))
non_serialized = "1,40,345,11294"
print(sys.getsizeof(non_serialized))


print("parsing")
parsed = robot_pb2.RobotData()
parsed.ParseFromString(serialized)
print(parsed)
