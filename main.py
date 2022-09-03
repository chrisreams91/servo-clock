import time
import busio
from board import SCL, SDA
from adafruit_pca9685 import PCA9685
from util import Segment, Digit


i2c = busio.I2C(SCL, SDA)
# You can optionally provide a finer tuned reference clock speed to improve the accuracy of the
# timing pulses. This calibration will be specific to each board and its environment. See the
# calibration.py example in the PCA9685 driver.
# pca = PCA9685(i2c, reference_clock_speed=25630710)
pcaHoursBoard = PCA9685(i2c, address=0x40)
pcaMinutesBoard = PCA9685(i2c, address=0x41)

pcaHoursBoard.frequency = 50
pcaMinutesBoard.frequency = 50


# hoursDigitOneSegments = []
# for i in range(7):
#     segment = Segment(pcaMinutesBoard.channels[i], len(hoursDigitOneSegments))
#     hoursDigitOneSegments.append(segment)

hoursDigitTwoSegments = []
for i in range(8,15):
    segment = Segment(pcaHoursBoard.channels[i], len(hoursDigitTwoSegments))
    hoursDigitTwoSegments.append(segment)

minutesDigitOneSegments = []
for i in range(7):
    segment = Segment(pcaMinutesBoard.channels[i], len(minutesDigitOneSegments))
    minutesDigitOneSegments.append(segment)

minutesDigitTwoSegments = []
for i in range(8,15):
    segment = Segment(pcaMinutesBoard.channels[i], len(minutesDigitTwoSegments))
    minutesDigitTwoSegments.append(segment)


# hoursDigitOne = Digit(hoursDigitOneSegments)
hoursDigitTwo = Digit(hoursDigitTwoSegments)
minutesDigitOne = Digit(minutesDigitOneSegments)
minutesDigitTwo = Digit(minutesDigitTwoSegments)

for i in range(10):
    # hoursDigitOne.setNumber(i)
    hoursDigitTwo.setNumber(i)
    minutesDigitOne.setNumber(i)
    minutesDigitTwo.setNumber(i)
    time.sleep(3)


# hoursDigitOne.setOff()
hoursDigitTwo.setOff()
minutesDigitOne.setOff()
minutesDigitTwo.setOff()

pcaHoursBoard.deinit()
pcaMinutesBoard.deinit()
