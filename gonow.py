
import hours,colors
from led import pixels
from icecream import ic

places=["282655576","4143672011","4153947940","3913401397"]
lat=47.49973
lon=8.72413

for i,place in enumerate(places):
    oh=hours.get_by_id(place,lat,lon)
    #print(f"{place} => open: {oh.is_open()}, next: {oh.next_change()}")
    ic(oh)
    if not oh["is_open"]:
        pixels[i]=colors.RED.rgb
    else:
        pixels[i]=colors.GREEN.rgb