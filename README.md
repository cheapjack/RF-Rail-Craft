# RF-Rail-Craft

### Code and make files for MOSI/FACT Lever Prize Installation

![No Of Participants](https://img.shields.io/badge/participants%20estimate-630-brightgreen.svg)

![rfrailcraft1](https://cloud.githubusercontent.com/assets/128456/17853611/905fe902-6865-11e6-85e0-c6b2cbde2655.jpg)
![rfrailcraft2](https://cloud.githubusercontent.com/assets/128456/17854274/50024720-6869-11e6-8061-583f26352347.jpg)


### Getting Started

For the radio controlled elements in `trainButtons.py` you'll need an [RF-Craft](https://github.com/cheapjack/RF-Craft) Receiver/Transmitter Pair, but you can also just run `trainBuilder.py` and `trainDriver.py` on a Raspberry Pi with Raspbian Jessie on it and clone this repo with it's inculded `mcpi` folder from the always awaesome [Martin O'Hanlon](https://github.com/martinohanlon)

Raise an [issue](http://cheapjack.github.io/2016/08/09/rf-craft-to-railcraft/issues) on the **RF-Craft** repo if you're an educator interested in testing the first batch.

After cloning the repo which I've described in my [RF-Rail-Craft Blogpost](http://cheapjack.github.io/2016/08/09/rf-craft-to-railcraft) you need to get rid of the standard minecraft world and add the trainworld archive 

`pi$ cd ~/.minecraft/games/com.mojang/minecraftworlds/`

`pi$ rm -rf world/`

`pi$ mv ~/RF-Rail-Craft trainworld2.tar.gz .`

then uncompress it with `tar`

`pi$ tar -zxvf trainworld2.tar.gz`

Then open up a minecraft game and `Start` the trainworld

Now run `trainDriver.py` or `trainBuilder.py` or `trainButtons.py` from your **RF-Rail-Craft** directory to control the trains and workshop.s

## trainBuilder

For the workshop we used `trainBuilder.py` code on one Raspbian image and then used a [5 port ethernet switch](http://www.amazon.co.uk/dp/B0000E5SEQ) & 5 CAT5 1m cables to network 4 more **Pis** together. 

The Pi with the code running became the `server` so we started that minecraft game first after using the WiFi/eth0 dropdown menu in `startx` to set a fixed `ipaddress` of `192.168.0.25` with a router address of `192.168.0.1`. After a reboot, this was set and then we configured
all the other **pis** in the same way with addresses  `192.168.0.26 - 29` and the same router address of `192.168.0.1`. All the other settings where left blank so they could remain as defaults. You need to reboot with them connected up to the switch after applying these settings.

Now in each `client` **Pi** we start a minecraft game but **DO NOT** create a new world, we use the `Join Game` option in the **Minecraft PI** start menu and join the world marked

```
StevePi
192.168.0.25
```

Now you can run the `trainBuilder.py` code, ensure the player is flying in the game on the `192.168.0.25` **Pi** and that player's camera will make it look like the train is moving while everyone else can build.

I've only dared try it with 5 networked Pi 2's & 3's so Id probably consider over-clocking the server Pi with additional [heatsinks](https://www.raspberrypi.org/forums/viewtopic.php?f=91&t=99525) if you wanted to try it on more.

![AllAboardImage](https://github.com/cheapjack/RF-Rail-Craft/blob/master/images/RF-Rail-Craft.png)

