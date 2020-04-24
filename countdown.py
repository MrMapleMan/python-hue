import sys
import time
import datetime

timeout = float(sys.argv[1])

t1 = time.time()

while time.time() - t1 < timeout:
  s = '\r' + str(datetime.datetime.now())
  s += ' time remaining: %.3f' % (t1+timeout - time.time() )
  sys.stdout.write(s)
  sys.stdout.flush()
  time.sleep(.01)
print ''
