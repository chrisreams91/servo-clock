## Cycle through all numbers for calibration purposes
import time
from util import initialize

hoursDigitOne, hoursDigitTwo, minutesDigitOne, minutesDigitTwo = initialize()

hoursDigitOne.setOff()
hoursDigitTwo.setOff()
minutesDigitOne.setOff()
minutesDigitTwo.setOff()

time.sleep(3)

for i in range(10):
    hoursDigitOne.setNumber(i)
    hoursDigitTwo.setNumber(i)
    minutesDigitOne.setNumber(i)
    minutesDigitTwo.setNumber(i)
    time.sleep(2)
