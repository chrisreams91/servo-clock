import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from util import Segment, Digit, digitOffsetMap


i2c = busio.I2C(SCL, SDA)
pcaHoursBoard = PCA9685(i2c, address=0x40)
pcaMinutesBoard = PCA9685(i2c, address=0x41)

pcaHoursBoard.frequency = 50
pcaMinutesBoard.frequency = 50


hoursDigitOneSegments = []
for i in range(7):
    segment = Segment(pcaHoursBoard.channels[i], len(hoursDigitOneSegments), digitOffsetMap["hours"]["digitOne"][i])
    hoursDigitOneSegments.append(segment)

hoursDigitTwoSegments = []
for i in range(8,15):
    segment = Segment(pcaHoursBoard.channels[i], len(hoursDigitTwoSegments), digitOffsetMap["hours"]["digitTwo"][i])
    hoursDigitTwoSegments.append(segment)

minutesDigitOneSegments = []
for i in range(7):
    segment = Segment(pcaMinutesBoard.channels[i], len(minutesDigitOneSegments), digitOffsetMap["minutes"]["digitOne"][i])
    minutesDigitOneSegments.append(segment)

minutesDigitTwoSegments = []
for i in range(8,15):
    segment = Segment(pcaMinutesBoard.channels[i], len(minutesDigitTwoSegments), digitOffsetMap["minutes"]["digitTwo"][i])
    minutesDigitTwoSegments.append(segment)


hoursDigitOne = Digit(hoursDigitOneSegments)
hoursDigitTwo = Digit(hoursDigitTwoSegments)
minutesDigitOne = Digit(minutesDigitOneSegments)
minutesDigitTwo = Digit(minutesDigitTwoSegments)


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