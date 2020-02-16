import socket
from object_pb2 import ObjectData

class Robot:
    def __init__(self, rid=0, team=1, color=None, sock=None):
        self.id = rid
        self.team = team
        self.color = ""
        self.x = 0
        self.y = 0
        self.yaw = 0
        self.socket = sock
    
    def set_socket(sock):
        self.socket = sock


class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0

class State:
    def __init__(self, home_robots=[], away_robots=[], ball=Ball()):
        """
            Global state of the match
        """
        
        self.home_robots = home_robots
        self.away_robots = away_robots
        self.ball = ball

        self.status = 0
        self.home_goals = 0
        self.away_goals = 0

    def update(self, serialized):
        """
        serialized: serialized data from protobuffer.SerializeToString()
        """
        deserialized = ObjectData()
        deserialized.ParseFromString(serialized)
        print(deserialized)
        
        if deserialized.kind == 1:
            # Robot
            self.home_robots[deserialized.id].x = deserialized.x
            self.home_robots[deserialized.id].y = deserialized.y
            self.home_robots[deserialized.id].yaw = deserialized.yaw

        elif deserialized.kind == 2:
            # Ball
            print("ball")
