from time import sleep

import colors
import platform

if platform.system() == 'Linux':
    import board
    import neopixel
else:
    from mock import mock_board as board, mock_neopixel as neopixel
from const import NUM_SLOTS, MAX_TRIES

import logging
logger = logging.getLogger('paniclog')

class Led:
    DATA_PIN = board.D18
    pixels = neopixel.NeoPixel(DATA_PIN, NUM_SLOTS + MAX_TRIES, brightness=0.5, pixel_order=neopixel.RGB)

    def __init__(self, index):
        self.index = index
        self.previous_color = colors.BLACK

    def set(self, color):
        logger.debug("LED " + str(self.index) + ":" + color.symbol)
        Led.pixels[self.index] = color.rgb

    def set_blueized(self, color):
        self.previous_color = Led.pixels[self.index]
        Led.pixels[self.index] = (color.rgb[0],color.rgb[1],color.rgb[2]+75)
        
    def debluize(self):
        Led.pixels[self.index] =self.previous_color
        
    def on(self):
        self.set(colors.WHITE)

    def off(self):
        self.set(colors.BLACK)



    @staticmethod
    def animate_loss(times=5):
        logger.info("🔴🔴🔴 LOSS 🔴🔴🔴")
        for i in range(times):
            for j in range(len(Led.pixels)):
                Led.pixels[j] = colors.RED.rgb
            sleep(0.6)
            for j in range(len(Led.pixels)):
                Led.pixels[j] = colors.BLACK.rgb
            sleep(0.3)
        logger.debug("animation end")
            
    @staticmethod
    def animate_fatal():
        while True:
            Led.animate_loss()

    @staticmethod
    def animate_win(times=10):
        logger.info("🟢🟢🟢 WIN 🟢🟢🟢")
        for i in range(times):
            for j in range(NUM_SLOTS):
                Led.pixels[j]= colors.GREEN.rgb
                sleep(0.2)
            sleep(0.5)
            for j in range(NUM_SLOTS):
                Led.pixels[j] = colors.BLACK.rgb
        logger.debug("animation end")

    @staticmethod
    def reset():
        for i in range(len(Led.pixels)):
            Led.pixels[i] = colors.BLACK.rgb

    @staticmethod
    def set_all(color):
        for i in range(len(Led.pixels)):
            Led.pixels[i] = color.rgb


if __name__ == '__main__':
    index = int(input("LED Nr.:"))
    led = Led(index)
    led.set(colors.GREEN)
    print("led should now be green")
    input("Press Enter to turn off...")
    led.set(colors.BLACK)
