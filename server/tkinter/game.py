import socket

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
        self.status = 0
        self.home_robots = home_robots
        self.away_robots = away_robots
        self.ball = ball

        self.home_goals = 0
        self.away_goals = 0
