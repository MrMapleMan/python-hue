from phue import Bridge
import time
import datetime
import sys

# Get light object
light = Bridge('192.168.0.190')['Bedside Lamp']
brightnessStart = light.brightness
print('Initial brightness: %d.' % brightnessStart)

countdownMinutes = int(sys.argv[1])  # How long the timer should run, in minutes
countdownSeconds = countdownMinutes*60

startTime = time.time()
endTime = startTime + countdownSeconds

print('Start: ' + str(datetime.datetime.fromtimestamp(startTime)) + '\tEnd: ' + 
      str(datetime.datetime.fromtimestamp(endTime)) )

divisions = 60
divisionTime = (endTime - startTime)/divisions

nextDivisionTime = startTime + divisionTime
print('First update: %s' % str(datetime.datetime.fromtimestamp(nextDivisionTime)) )

# TODO: remove after testing
firstFraction = (nextDivisionTime - endTime) / (startTime - endTime)
firstBrightness = int((nextDivisionTime - endTime) / (startTime - endTime) * brightnessStart)
print('firstFraction: %.2f\tfirstBrightness: %d' %(firstFraction, firstBrightness) )

while time.time() < endTime:
  # Check if update timer has passed
  if time.time() > nextDivisionTime:
    # Readjust light brightness
    brightnessInterpolated = (time.time() - endTime) / (startTime - endTime) * brightnessStart
    light.brightness = int( brightnessInterpolated )
    # Update division time
    nextDivisionTime += divisionTime
    nextDivisionTimeString = str(datetime.datetime.fromtimestamp(nextDivisionTime))
    print('nextDivisionTime passed. New brightness: %3d. Next update: %s' %(light.brightness, nextDivisionTimeString))
  # Sleep to reduce compute load
  time.sleep(2)

# Countdown has ended: turn off light
light.on = False
