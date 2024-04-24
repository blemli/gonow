# gonow
_is it still open or not?_![G0075](assets/G0075.svg)

## use
1. Plug in PoE-Cable
2. Wait 20 Seconds
3. Go to http://gonow.local and
4. enter some Locations
5. Label the corresponding LED's
6. enjoy!

## features

- 18 nice, soft glowing led's
- turns off at night (bedroom compatible)
- only public apis used (no credentials needed)
- configurable via browser

## maintain 

connect: `ssh pi@vrminutes.local`  (only key, no password access)

- `follow`  follows live logs
- `errors` shows latest errors
- `sudo service vrminutes start/stop/restart`
- `disable` or  `enable` the service

## install

On the pi:

1. generate key:  `ssh-keygen -o -t ed25519 -f ~/.ssh/id_ed25519 -C "gonow.local" -P ""` 
2. create Installation directory `sudo mkdir /opt/gonow && sudo chown -c pi /opt/gonow`
3. install git: `sudo apt install -y git`

Your Machine:

1. navigate into to the repository directory: `cd gonow`
2. copy the public key from the raspberry: `scp gonow:~/.ssh/id_ed25519.pub .`
3. give the key read rights: `gh repo deploy-key add id_ed25519.pub`
4. clean up: `rm id_ed25519.pub`

Finally, on the pi again:

1. `git clone https://github.com/blemli/gonow.git /opt/gonow`
2. install: `cd /opt/gonow && chmod +x setup/*.sh && setup/setup.sh`

## parts

- 1 ×    [Raspberry Pi 4, 2GB](https://www.digikey.ch/de/products/detail/raspberry-pi/SC0193-9/10258782) (39.60)
- 1 ×    [SD-Card](https://alltron.ch/de/product/1131343) (12.45)
- 1 ×    [UniPi HighPi Case](https://www.pi-shop.ch/highpi-gehaeuse-schwarz) (17.90)
- 1 ×    [Tesa ZOOM](https://alltron.ch/de/product/339023) inkl. Strip(13.-)
- 18 × [Neopixel WS2812 RGB LED, PTH, 5mm, diffus](https://www.digikey.ch/de/products/detail/sparkfun-electronics/COM-12986/5673799) (12.32)
- 1 ×    [Raspberry Pi PoE HAT](https://www.digikey.ch/de/products/detail/raspberry-pi/SC1022/14313703) (17.6)
- 1 ×    [Stacking Header](https://www.digikey.ch/de/products/detail/adafruit-industries-llc/1979/6238003)(2.6)
- 1 ×    [4-Way-Riser](https://www.digikey.ch/de/products/detail/samtec-inc/SSQ-102-01-G-D/1110568) (0.93)
- misc cables

Total: 116.4