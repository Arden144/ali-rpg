from itertools import zip_longest

from keypress import keypress
from util import clear


def columnify(*text, sep=" | "):
    parts = [x.splitlines() for x in text]
    lengths = [max(map(len, x)) for x in parts]
    for line in zip_longest(*parts, fillvalue=""):
        yield sep.join(
            content.ljust(length) for content, length in zip(line, lengths)
        )


def choose(message, options, caps=False):
    fmt_options = [x.capitalize() if caps else x for x in options]
    length = max(20, max(map(len, options)))
    selected = 0
    while True:
        clear()

        info = ""
        for i, option in enumerate(fmt_options):
            if i == selected:
                info += "-" * (length + 4) + "\n"
                info += f"| {option.ljust(length)} |\n"
                info += "-" * (length + 4) + "\n"
            else:
                info += "\n"
                info += f"  {option}\n"
                info += "\n"

        print("\n".join(columnify(message, info)))

        key = keypress("", ["up", "down", "enter"])

        if key == "enter":
            return options[selected]
        if key == "up" and selected > 0:
            selected -= 1
        if key == "down" and selected < len(options) - 1:
            selected += 1
