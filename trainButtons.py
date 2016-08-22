#!/usr/python

# import mcpi, you will need the mcpi directory to be local to the trainButtons.py ie in the same directory.
from mcpi import minecraft
from time import sleep
import serial

# connect to the game locally, ie on your pi
mc = minecraft.Minecraft.create()
# or specify a server and optionally, a port
#mc = minecraft.Minecraft.create("mc.fact.co.uk")

# Make sure you release the serial port using
# pi$ raspi-config
# and disable the shell and kernel messages to serial its option A8 in the (9) Advanced Options MENU
# Otherwise the port will be used elsewhere

ser = serial.Serial('/dev/ttyAMA0', 9600)
mc.postToChat("Connected to mcpi Serial says " + str(ser.name))
red_button_received = "1,1\r\n"
yellow_button_received = "2,1\r\n"
green_button_received = "3,1\r\n"
blue_button_received = "4,1\r\n"
# clear area option
#mc.setBlocks(94, 1 ,126,-127 ,10, -99, 0, 0)

def clearTrain(xpos, ypos, zpos, length,height, width):
    mc.setBlocks(xpos, ypos, zpos, xpos, ypos+height, zpos + width,0, 0)

#Find my entityId for the first spawned player
entityIds = mc.getPlayerEntityIds()
trainPOV = entityIds[0]
#trainSpotter = entityIds[1]
print trainPOV
trainPOVTilePos = mc.entity.getTilePos(trainPOV)
#Make the camera follow the player
#mc.camera.setFollow(trainSpotter)
#mc.camera.setFixed()
mc.camera.setNormal()

# Send a message to minecraft console
mc.postToChat("Hello Minecraft World!")
mc.postToChat("We need to listen to buttons!")
# Clear the track
#mc.postToChat("Clear the line")

mc.postToChat("Waiting for buttons!")

#loop until Ctrl C
try:
    while(True):
        moving = False
        #define serialcommand
        serialcommand = str(ser.readline())
        if serialcommand == green_button_received:
            mc.postToChat("Green Pressed")
            mc.postToChat("Go! lets feel the speed!")
            mc.camera.setFixed(trainPOV)
            print("green/1 Pressed")
            mc.camera.setNormal()
        elif serialcommand == red_button_received:
            mc.postToChat("Red Pressed")
            print("red/1 Pressed")
            mc.postToChat("We can't stop the train or we'll be late!")
        elif serialcommand == yellow_button_received:
            mc.postToChat("Yellow pressed")
            mc.postToChat("Let's have a look from above!")
            print("Yellow/2 Pressed")
            mc.camera.setFollow(trainPOV)
            trainPOVTilePos = mc.entity.getTilePos(trainPOV)
            mc.entity.setTilePos(trainPOV, trainPOVTilePos.x+6, trainPOVTilePos+8, trainPOVTilePos )
            sleep(0.5)
        elif serialcommand == blue_button_received::
            mc.postToChat("Blue pressed")
            mc.postToChat("Blue pressed")
            mc.camera.setNormal(trainPOV)
            print("Blue Pressed")

except KeyboardInterrupt:
    print("stopped")
finally:
    #stop everything
    #track.stop()
    ser.close()
