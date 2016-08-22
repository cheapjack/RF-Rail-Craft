# RF-Rail-Craft

![No Of Participants](https://img.shields.io/badge/participants%20estimate-630-brightgreen.svg)

![rfrailcraft1](https://cloud.githubusercontent.com/assets/128456/17853611/905fe902-6865-11e6-85e0-c6b2cbde2655.jpg)
![rfrailcraft2](https://cloud.githubusercontent.com/assets/128456/17854274/50024720-6869-11e6-8061-583f26352347.jpg)

Code and make files for MOSI/FACT Lever Prize Installation

### Getting Started

You'll need an [RF-Craft](https://github.com/cheapjack/RF-Craft) Receiver/Transmitter Pair, a Raspberry Pi with Raspbian Jessie on it and clone this repo with it's inculded `mcpi` folder from the always awaesome [Martin O'Hanlon](https://github.com/martinohanlon)

After cloning the repo which I've described in my [RF-Rail-Craft Blogpost](http://cheapjack.github.io/2016/08/09/rf-craft-to-railcraft) you need to get rid of the standard minecraft world and add the trainworld archive 

`pi$ cd ~/.minecraft/games/com.mojang/minecraftworlds/`

`pi$ rm -rf world/`

`pi$ mv ~/RF-Rail-Craft trainworld2.tar.gz .`

then uncompress it

`pi$ tar -zxvf trainworld2.tar.gz`

Then open a minecraft game and enter the trainworld

Now run `trainDriver.py` or `trainBuilder.py` or `trainButtons.py` to control the trains and workshops

![AllAboardImage](https://github.com/cheapjack/RF-Rail-Craft/blob/master/images/RF-Rail-Craft.png)

