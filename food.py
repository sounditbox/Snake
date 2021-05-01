from game_object import GameObject


class Food(GameObject):
    def __init__(self, x, y, worth):
        super().__init__(x, y)
        self.worth = worth
