from phue import Bridge
import random
import time
import sys

# Example usage: python setBedsideLamp.py .52 .45 200

# ================ CHANGE THESE =================
bridgeIP = '192.168.0.190'
lightNames = ['Bedside Lamp']
# ===============================================

# For trying different color schemes
def randomColors():
  x = r()
  y = r()
  print "x: %.3f y: %.3f" %(x,y)
  for i in lights:
    i.xy = (x,y)

# Initialize Bridge object
b = Bridge(bridgeIP)

# If running for the first time: uncomment below and start within 30 seconds of pressing Hue bridge button
# b.connect()

# Get lights from bridge
lights = b.get_light_objects()

# Rename random function for convenience
r = random.random

# Find indeces of lights not targeted for this command
indeces = []
for ind,i in enumerate(lights):
  if i.name not in lightNames:
    indeces.append(ind)
# Discard lights that were not specified in lightNames
for i in range(len(indeces)-1,-1,-1):
  lights.pop(indeces[i])

'''
# Try random xy combinations to explor color space
for i in range(5):
  randomColors()
  time.sleep(1)
'''

# Set lights to xy colors and brightness passed to script in arguments
for i in lights:
  xy = (float(sys.argv[1]),float(sys.argv[2]))
  brightness = int(sys.argv[3])
  wasOn = i.on
  if brightness == 0:
    i.on = False
    break
  elif not wasOn:
    i.on = True
  i.xy = xy
  i.brightness = brightness

