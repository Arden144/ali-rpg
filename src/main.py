from map import Map
from menu import choose


class Game:
    state = "menu"

    def __init__(self):
        self.player_pos = (0, 0)
        self.map = Map(self.get_player_pos)
        self.run_state = {
            "menu": self.menu,
            "moving": self.moving,
        }

    def get_player_pos(self):
        return self.player_pos

    def menu(self):
        choice = choose(str(self.map), ["start", "help", "quit"], caps=True)
        if choice == "start":
            self.state = "moving"
        elif choice == "quit":
            self.state = "quit"

    def moving(self):
        pass

    def play(self):
        while self.state != "quit":
            self.run_state[self.state]()


def main():
    game = Game()
    game.play()


if __name__ == "__main__":
    main()
