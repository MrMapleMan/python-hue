from phue import Bridge
import time
import datetime
import sys

# Get light object
light = Bridge('192.168.0.190')["Jessi's Lamp"]

isOn = light.on

if len(sys.argv) < 2:
  # Display brightness
  currentBrightness = light.brightness
  print('Current brightness is %.1f%% (%d/255).' % (float(currentBrightness)/255.*100., currentBrightness) )
  # Display instructions for use and exit
  print('To set brightness, pass desired %. Example: "python setBedsideBrightness.py 15.5"')
  sys.exit()

# Retrieve desired percentage, map to 8-bit
brightnessPercent = float(sys.argv[1])
brightnessSetting = int(round(brightnessPercent*255/100.0))
print('Brightness set: %.1f%% (%d/255).' % (brightnessPercent,brightnessSetting) )

# Readjust light brightness
if not isOn:
  light.on = True
light.brightness = brightnessSetting

# Light set to 0: turn off light
if brightnessSetting == 0:
  light.on = False
