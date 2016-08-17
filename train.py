#!/usr/python

# import mcpi, you will need the mcpi directory to be local to the carriage.py ie in the same directory.
from mcpi import minecraft

# connect to the game locally, ie on your pi
#mc = minecraft.Minecraft.create()
mc = minecraft.Minecraft.create("mc.fact.co.uk")

#Define a Carriage function

def CarriageTemplate(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType):
    # main carriage chassis
    for i in range(1,numberOfCarriages):
        mc.setBlocks(xpos + (i*length) + 1, ypos + 1, zpos, (xpos+(i*length)) + length + 1, ypos + 1, zpos + width, material, materialType)
        #Make gaps
        mc.setBlocks(xpos + (i*length) + length, ypos + 1, zpos, xpos + (i*length) + length, ypos + 1, zpos + width, 0)
        # Make 4 wheels
        mc.setBlock(xpos + (i*length) + 1, ypos, zpos - 1, 89)
        mc.setBlock(xpos + (i*length) + length - 1, ypos, zpos - 1, 89)
        mc.setBlock(xpos + (i*length) + 1, ypos, zpos + (width + 1), 89)
        mc.setBlock(xpos + (i*length) + length - 1, ypos, zpos + (width + 1), 89)

#Define a Train function

def Train(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType):
    # Build the carriage behind us
    CarriageTemplate(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType)
    # wood engine base
    mc.setBlocks(xpos, ypos + 2, zpos, xpos + length, ypos + 2 , zpos + width, 5, 0)
    mc.setBlocks(xpos, ypos + 3, zpos - 1, xpos + length, ypos + 3 , zpos + width + 1, 5, 0)
    # next 2 layers iron and facia
    mc.setBlocks(xpos, ypos + 4, zpos - 1, xpos + length, ypos + 5 , zpos + width + 1, 42, 0)
    mc.setBlocks(xpos, ypos + 6, zpos, xpos + length, ypos + 4 , zpos + width, 42, 0)
    mc.setBlocks(xpos, ypos + 3, zpos - 1, xpos + 1, ypos + 5 , zpos + width, 42, 0)
# gold front
    mc.setBlocks(xpos + 1, ypos + 3, zpos + 1, xpos + 1, ypos + 5 , zpos + 1, 41, 0)
    mc.setBlocks(xpos, ypos + 4, zpos, xpos, ypos + 4 , zpos + width, 41, 0)
    mc.setBlock(xpos - 1, ypos + 4, zpos + 1, 41, 0)
# chimney & chassis
    mc.setBlocks(xpos, ypos + 6, zpos + 1, xpos, ypos + 8, zpos + 1, 42, 0)
    mc.setBlocks(xpos, ypos + 1, zpos, xpos + length, ypos + 1, zpos + width, 42, 0)
    # Wheels
    mc.setBlock(xpos + 1, ypos, zpos - 1, 89)
    mc.setBlock(xpos + length - 1, ypos, zpos - 1, 89)
    mc.setBlock(xpos + 1, ypos, zpos + (width + 1), 89)
    mc.setBlock(xpos + length - 1, ypos, zpos + (width + 1), 89)



# Send a message to minecraft console
mc.postToChat("Hello Minecraft World!")
mc.postToChat("We need rolling stock!")
mc.postToChat("Lets get building carriages!")
playerTilePos = mc.player.getTilePos()
mc.postToChat("TilePos is " + str(playerTilePos))
# Remember our Carriage function above needs the values Starting xpos, ypos, zpos, length of carriage, width of carriage, numberOfCarriages, blockmaterial, blockmaterialType.
# Call our Carriage Function
#CarriageTemplate(playerTilePos.x+1, playerTilePos.y, playerTilePos.z+1, 6, 2, 4, 42, 0)
# Train takes StartXpos, ypos, zpos, length, width, numberOfCarriages, material,materialType):
mc.postToChat("Building Carriage chassis with engine at front!")
Train(playerTilePos.x,playerTilePos.y, playerTilePos.z, 7, 2, 4, 42, 0)
#print to minecraft console so we know what we did

