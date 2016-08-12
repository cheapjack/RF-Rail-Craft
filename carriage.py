#!/usr/python

# import mcpi, you will need the mcpi directory to be local to the carriage.py ie in the same directory.
from mcpi import minecraft

# connect to the game locally, ie on your pi
mc = minecraft.Minecraft.create()

#Define a Carriage function

def CarriageTemplate(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType):
    # main carriage chassis
    for i in range(1,numberOfCarriages):
        mc.setBlocks((xpos*i), ypos + 1, zpos, (xpos*i) + length, ypos + 1, zpos + width, material, materialtype)
        # Make 4 wheels
        mc.setBlock((xpos*i) + 2, ypos, zpos - 1), 89)
        mc.setBlock((xpos*i) + length - 2, ypos, zpos - 1, 89)
        mc.setBlock((xpos*i) + 2, ypos, zpos + (width + 1), 89)
        mc.setBlock((xpos*i) + length - 2, ypos, zpos + (width + 1), 89)
# Send a message to minecraft console
mc.postToChat("Hello Minecraft World!")
mc.postToChat("We need rolling stock!")
mc.postToChat("Lets get building carriages!")
playerTilePos = mc.player.getTilePos()
# Remember our Carriage function above needs the values Starting xpos, ypos, zpos, length of carriage, width of carriage, numberOfCarriages, blockmaterial, blockmaterialType.

CarriageTemplate(playerTilePos.x, playerTilePos.y, playerTilePos.z, 6, 2, 13, 1)
CarriageTemplate(10, 1, 10, 6, 2, 13, 1)
#print to minecraft console so we know what we did
mc.postToChat("Building " + str(numberOfCarriages) + " Carriage chassis!")


