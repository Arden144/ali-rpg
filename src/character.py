class Character:
    def __init__(
        self,
        position=(0, 0),
        inventory=[],
    ):
        self.inventory = inventory
        self.position = position

    def get_pos(self):
        return self.position
