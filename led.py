import board
import neopixel

import colors

LED_COUNT=18
DATA_PIN = board.D18
pixels = neopixel.NeoPixel(DATA_PIN, LED_COUNT, brightness=0.05, pixel_order=neopixel.RGB)

if __name__=="__main__":
    import time
    cols=[colors.GREEN.rgb,colors.RED.rgb,colors.WHITE.rgb,colors.PURPLE.rgb,colors.YELLOW.rgb]
    while True:
        for color in cols:
            for i in range(LED_COUNT):
                pixels[i]=color
                time.sleep(0.1)
