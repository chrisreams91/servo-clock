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


minutesDigitOneSegments = []
for i in range(8,15):
    segment = Segment(pcaMinutesBoard.channels[i], len(minutesDigitOneSegments))
    minutesDigitOneSegments.append(segment)

minutesDigitTwo = Digit(minutesDigitOneSegments)


minutesDigitTwo.setNumber(0)
time.sleep(.75)

minutesDigitTwo.setNumber(1)
time.sleep(.75)

minutesDigitTwo.setNumber(2)
time.sleep(.75)

minutesDigitTwo.setNumber(3)
time.sleep(.75)

minutesDigitTwo.setNumber(4)
time.sleep(.75)

minutesDigitTwo.setNumber(5)
time.sleep(.75)

minutesDigitTwo.setNumber(6)
time.sleep(.75)

minutesDigitTwo.setNumber(7)
time.sleep(.75)

minutesDigitTwo.setNumber(8)
time.sleep(.75)

minutesDigitTwo.setNumber(9)
time.sleep(.75)

minutesDigitTwo.setOff()



pcaHoursBoard.deinit()
pcaMinutesBoard.deinit()
