#!/usr/python

# import mcpi, you will need the mcpi directory to be local to the carriage.py ie in the same directory.
from mcpi import minecraft

# connect to the game locally, ie on your pi
mc = minecraft.Minecraft.create()

#Define a Carriage function

def CarriageTemplate(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType):
    length = length + 1
    # main carriage chassis
    for i in range(1,numberOfCarriages + 1):
        mc.setBlocks(xpos + (i*length) + 1, ypos + 1, zpos, (xpos+(i*length)) + length + 1, ypos + 1, zpos + width, material, materialType)
        #Make gaps
        mc.setBlocks(xpos + (i*length) + length, ypos + 1, zpos, xpos + (i*length) + length, ypos + 1, zpos + width, 0)
        # Make 4 wheels
        mc.setBlock(xpos + (i*length) + 2, ypos, zpos - 1, 57)
        mc.setBlock(xpos + (i*length) + length - 2, ypos, zpos - 1, 57)
        mc.setBlock(xpos + (i*length) + 2, ypos, zpos + (width + 1), 57)
        mc.setBlock(xpos + (i*length) + length - 2, ypos, zpos + (width + 1), 57)

# Send a message to minecraft console
mc.postToChat("Hello Minecraft World!")
mc.postToChat("We need rolling stock!")
mc.postToChat("Lets get building carriages!")
playerTilePos = mc.player.getTilePos()
mc.postToChat("TilePos is " + str(playerTilePos))
# Remember our Carriage function above needs the values Starting xpos, ypos, zpos, length of carriage, width of carriage, numberOfCarriages, blockmaterial, blockmaterialType.
# Call our Carriage Function
CarriageTemplate(playerTilePos.x+1, playerTilePos.y, playerTilePos.z+1, 6, 2, 4, 42, 0)
#print to minecraft console so we know what we did
mc.postToChat("Building Carriage chassis!")


