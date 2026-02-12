room_labels = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f'],
    ['g', 'h', 'j']
]

class Environment:
    def __init__(self):
        self.room_labels = room_labels
        self.room_status = {
            'a': 'safe',
            'b': 'safe',
            'c': 'fire',
            'd': 'safe',
            'e': 'fire',
            'f': 'safe',
            'g': 'safe',
            'h': 'safe',
            'j': 'fire'
        }

    def display(self):
        print("Environment status:")
        for row in self.room_labels:
            for room in row:
                if self.room_status[room] == 'fire':
                    print("f", end=" ")
                else:
                    print("-", end=" ")
            print()
        print()

class FireFightingRobot:
    def __init__(self, environment):
        self.env = environment
        self.path = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']

    def move_and_extinguish(self):
        for room in self.path:
            print(f"Robot enters room '{room}'.")
            if self.env.room_status[room] == 'fire':
                print(f"Fire detected in room '{room}'! Extinguishing fire...")
                self.env.room_status[room] = 'safe'
            else:
                print(f"Room '{room}' is safe.")
            self.env.display()
        print("Final environment status (all fires extinguished):")
        self.env.display()

# Instantiate environment and robot, then run
env = Environment()
robot = FireFightingRobot(env)
robot.move_and_extinguish()