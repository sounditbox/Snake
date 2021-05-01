from game_object import GameObject


class Snake(GameObject):
    def __init__(self, x, y, direction):
        super().__init__(x, y)
        self.direction = direction
        self.is_alive = True
        self.body = []
