import time
from util import initialize, Segment, Digit, digitOffsetMap

hoursDigitOne, hoursDigitTwo, minutesDigitOne, minutesDigitTwo = initialize()

# start animation
hoursDigitOne.setOff()
time.sleep(.2)
hoursDigitTwo.setOff()
time.sleep(.2)
minutesDigitOne.setOff()
time.sleep(.2)
minutesDigitTwo.setOff()
time.sleep(.5)

while True:
    hour = time.strftime('%I')
    minute = time.strftime('%M')

    if int(hour[0]) == 0:
        hoursDigitOne.setOff()
    else:
        hoursDigitOne.setNumber(int(hour[0]))

    hoursDigitTwo.setNumber(int(hour[1]))
    minutesDigitOne.setNumber(int(minute[0]))
    minutesDigitTwo.setNumber(int(minute[1]))
    time.sleep(5)