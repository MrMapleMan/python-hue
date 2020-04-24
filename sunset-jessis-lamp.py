from phue import Bridge
import time
import datetime
import sys

# Get light object
light = Bridge('192.168.0.190')["Jessi's Lamp"]
brightnessStart = light.brightness
print('Initial brightness: %d.' % brightnessStart)

countdownMinutes = float(sys.argv[1])  # How long the timer should run, in minutes
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

s = ''

while time.time() < endTime:
  # Check if update timer has passed
  if time.time() > nextDivisionTime:
    # Readjust light brightness
    brightnessInterpolated = (time.time() - endTime) / (startTime - endTime) * brightnessStart
    light.brightness = int( brightnessInterpolated )
    # Update division time
    nextDivisionTime += divisionTime
    nextDivisionTimeString = str(datetime.datetime.fromtimestamp(nextDivisionTime))
    if len(s) > 0:
      sys.stdout.write('\r' + ' '*len(s) + '\r')
      sys.stdout.flush()
    print ('nextDivisionTime passed. New brightness: %3d. Next update: %s' %(light.brightness, nextDivisionTimeString))

  s = "Current time: " + str(datetime.datetime.now()) + " Next time: " + \
      str(datetime.datetime.fromtimestamp(nextDivisionTime)) + \
      " Remaining: %.2f seconds." %(time.time() - nextDivisionTime)

  sys.stdout.write('\r' + s)
  sys.stdout.flush()
  # Sleep to reduce compute load
  time.sleep(.1)

# Countdown has ended: turn off light
light.on = False

print('\nCountdown completed and light turned off.  Good night!')
