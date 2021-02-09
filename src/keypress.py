# Code from Arden Sinclair
# used with permission
# https://github.com/ArdenSinclair/RPGGame


class GetKeyPress:
    def __init__(self):
        try:
            self.impl = _GetKeyPressWindows()
        except ImportError:
            self.impl = _GetKeyPressUnix()

    def __call__(self):
        ch = self.impl()
        if ch == "\x03":
            raise KeyboardInterrupt
        elif ch == "\x04":
            raise EOFError
        return ch


class _GetKeyPressWindows:
    def __init__(self):
        from msvcrt import getch

        self.getch = getch

    def __call__(self):
        ch = self.getch()
        if ch == b"\x00":
            ch = self.getch()
            if ch == b"H":
                return "up"
            elif ch == b"P":
                return "down"
            elif ch == b"K":
                return "left"
            elif ch == b"M":
                return "right"

        if ch == b"\r":
            return "enter"

        try:
            return ch.decode()
        except:
            if ch == b"\x03":
                return "\x03"
            elif ch == b"\x04":
                return "\x04"
            else:
                raise AttributeError("Error getting keypress from Windows")


class _GetKeyPressUnix:
    def __init__(self):
        from sys import stdin

        self.stdin = stdin
        from tty import setraw

        self.setraw = setraw
        from termios import TCSADRAIN, tcgetattr, tcsetattr

        self.tcgetattr, self.tcsetattr = tcgetattr, tcsetattr
        self.TCSADRAIN = TCSADRAIN

    def __call__(self):
        fd = self.stdin.fileno()
        old_settings = self.tcgetattr(fd)
        try:
            self.setraw(fd)
            raw_settings = self.tcgetattr(fd)
            raw_settings[1] = old_settings[1]
            self.tcsetattr(fd, self.TCSADRAIN, raw_settings)
            ch = self.stdin.read(1)
        finally:
            self.tcsetattr(fd, self.TCSADRAIN, old_settings)
        return ch


get_keypress = GetKeyPress()


def keypress(message, filter=None):
    print(message, end="", flush=True)
    while True:
        key = get_keypress()
        if filter and key not in filter:
            continue
        return key