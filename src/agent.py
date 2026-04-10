class Agent:
    def __init__(self, start):
        self.position = start

    def move(self, next_pos):
        self.position = next_pos