import board
import neopixel

import colors

LED_COUNT=4
DATA_PIN = board.D18
pixels = neopixel.NeoPixel(DATA_PIN, LED_COUNT, brightness=0.01, pixel_order=neopixel.RGB)

if __name__=="__main__":
    for i in range(LED_COUNT):
        pixels[i]=colors.RED.rgb