#!/usr/python

# import mcpi, you will need the mcpi directory to be local to the carriage.py ie in the same directory.
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
#ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=0, parity=serial.PARITY_EVEN, rtscts=1)
mc.postToChat("Connected to mcpi Serial says " + str(ser.name))
green_button_received = "3,1\r\n"
#clear area
#mc.setBlocks(94, 1 ,126,-127 ,10, -99, 0, 0)


#Define a track function

def Track(xpos, ypos, zpos, length, width, material, materialType):
    #put grass on the floor
    mc.setBlocks(xpos, ypos-1, zpos-1, xpos + length, ypos-1, zpos + width + 1, 2 ,0)
# iron track
    mc.setBlocks(xpos, ypos-1, zpos, xpos + length, ypos-1, zpos + width, material, materialType)
    # gaps in track
    for i in range(1, length, 1):
        mc.setBlocks(xpos, ypos-1, zpos+1, xpos + i, ypos-1, zpos + width-1, 4, 0)


#Define a Carriage function

def CarriageTemplate(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType):
    length = length + 1
    # main carriage chassis
    for i in range(numberOfCarriages+1):
        #chassis
        mc.setBlocks(xpos + (i*length) + 1, ypos + 1, zpos, (xpos+(i*length)) + length + 1, ypos + 1, zpos + width, material, materialType)
        #Make gaps
        mc.setBlocks(xpos + (i*length) + length, ypos + 1, zpos, xpos + (i*length) + length, ypos + 1, zpos + width, 0)
        # Make air above the chassis
        mc.setBlocks(xpos, ypos + 2, zpos-1, (xpos+(i*length)) + length + 1, ypos + 8, zpos + width+1, 0, 0)
        # Make 4 wheels
        # 1
        mc.setBlock(xpos + (i*length), ypos, zpos - 1, 0,0)
        mc.setBlock(xpos + (i*length) + 2, ypos, zpos - 1, 57)
        # Air gap
        mc.setBlocks(xpos + (i*length) + 3, ypos, zpos - 1, xpos + (i*length)+length-3, ypos, zpos -1, 0, 0)
        # 2
        mc.setBlock(xpos + (i*length) + length, ypos, zpos - 1, 0)
        mc.setBlock(xpos + (i*length) + length-1, ypos, zpos - 1, 0)
        mc.setBlock(xpos + (i*length) + length - 2, ypos, zpos - 1, 57)
        # 3
        mc.setBlock(xpos + (i*length), ypos, zpos + (width + 1), 0)
        mc.setBlock(xpos + (i*length) + 2, ypos, zpos + (width + 1), 57)
        # Air gap
        mc.setBlocks(xpos + (i*length) + 3, ypos, zpos +(width+1), xpos + (i*length)+length-3, ypos, zpos + (width+1), 0, 0)
        # 4
        mc.setBlock(xpos + (i*length) + length, ypos, zpos + (width + 1), 0)
        mc.setBlock(xpos + (i*length) + length-1, ypos, zpos + (width + 1), 0)
        mc.setBlock(xpos + (i*length) + length - 2, ypos, zpos + (width + 1), 57)
        if i == numberOfCarriages:
            #print "reached end of numberOfCarriages range"
            mc.setBlocks(xpos + (i*length) + numberOfCarriages + length, ypos + 1, zpos, (xpos+(i*length)) + numberOfCarriages + length + 3, ypos + 2, zpos + width, 0, 0)


#Define a Train function

def Train(xpos, ypos, zpos, length, width, numberOfCarriages, material, materialType):
    #Build the carriage chassis behind us
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
    # Cabin
    mc.setBlocks(xpos + length-1, ypos+6, zpos + 1,xpos+length, ypos+6, zpos+1, 0, 0)
    # chimney
    mc.setBlocks(xpos, ypos + 6, zpos + 1, xpos, ypos + 8, zpos + 1, 42, 0)
    #mc.setBlocks(xpos, ypos + 1, zpos, xpos + length, ypos + 1, zpos + width, 42, 0)
    # Wheels
    # 1
    mc.setBlock(xpos, ypos, zpos - 1, 0)
    mc.setBlock(xpos + 1, ypos, zpos - 1, 57)
    # 2
    mc.setBlock(xpos + length, ypos, zpos - 1, 0)
    mc.setBlock(xpos + length - 1, ypos, zpos - 1, 57)
    #3
    mc.setBlock(xpos, ypos, zpos + (width + 1), 0)
    mc.setBlock(xpos + 1, ypos, zpos + (width + 1), 57)
    #4
    mc.setBlock(xpos + length, ypos, zpos + (width + 1), 0)
    mc.setBlock(xpos + length - 1, ypos, zpos + (width + 1), 57)

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
mc.postToChat("We need a track!")
# Clear the track
#mc.postToChat("Clear the line")
mc.setBlocks(-158, 12, 35, 200, 21, 39, 0,0)
# Build a track
#Track(-158, 12, 35, 250, 4, 42, 0)
# Build a viaduct
#mc.setBlocks(92, -8, 34, -157, 10, 40, 4, 0)


# Build a static train
Train(67, 12, 36, 6, 2, 4, 42, 0)


# Remember our Carriage function above needs the values Starting xpos, ypos, zpos, length of carriage, width of carriage, numberOfCarriages, blockmaterial, blockmaterialType.
# Call our Carriage Function
# Train takes StartXpos, ypos, zpos, length, width, numberOfCarriages, material,materialType):
mc.postToChat("Waiting for buttons!")
#print to minecraft console so we know what we did
mc.postToChat("Lets get building a train!")

#loop until Ctrl C
try:
    while(True):
        moving = False
        #define serialcommand
        mc.postToChat("Ok All aboard! Starting Train!")
        print("Green Pressed")
        mc.camera.setNormal()
        moving = True
        direction = 1
        #mc.postToChat("direction = " + str(direction))
        lastpos = 0
        for i in range(130):
            if direction == 1:
                Train(67 - i, 12, 36, 6, 2, 4, 42, 0)
                #sleep(0.5)
                #mc.postToChat("update lastpos")
                lastpos = i - 1
                # remove previous trailing blocks
                clearTrain(67 + lastpos, 12, 36, 6, 2, 8)
                #mc.postToChat("clear trail")
                sleep(0.5)
            elif direction == -1:
                Train(-67 + i, 12, 36, 6, 2, 4, 42, 0)
                #sleep(0.5)
                #mc.postToChat("update lastpos")
                lastpos = i + 1
                # remove previous trailing blocks
                clearTrain(67 - lastpos, 12, 36, 6, 2, 8)
                #mc.postToChat("clear trail")
                sleep(0.5)
            elif i >= 129:
                mc.postToChat("Stopped!")
                sleep(3)
                mc.postToChat("Back to Manchester!")
                direction = direction * -1
                mc.postToChat("direction = " + str(direction))
            #track.startCar(1)
            sleep(0.5)
        except KeyboardInterrupt:
    print("stopped")
finally:
    #stop everything
    #track.stop()
    ser.close()


