# -*- coding: utf-8 -*-

"""
This file contains the Color class, which is used to represent colors in the
system. It is mostly used by the LED. But each slot-state has a corresponding color as well.
Purple is not used yet, but it is defined for future use :)
"""


class Color:
    def __init__(self, rgb, name, symbol):
        self.rgb = rgb
        self.name = name
        self.symbol = symbol


RED = Color((255, 0, 0), "red", "🔴")
GREEN = Color((0, 255, 0), "green", "🟢")
WHITE = Color((255, 255, 255), "white", "⚪")
BLACK = Color((0, 0, 0), "black", "⚫")
YELLOW = Color((200, 100, 0), "yellow", "🟡")
PURPLE = Color((255, 0, 255), "purple", "🟣")
