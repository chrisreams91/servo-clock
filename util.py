from adafruit_motor import servo

numberMap = {
    0: [1,1,1,0,1,1,1],
    1: [0,0,1,0,0,1,0],
    2: [1,0,1,1,1,0,1],
    3: [1,0,1,1,0,1,1],
    4: [0,1,1,1,0,1,0],
    5: [1,1,0,1,0,1,1],
    6: [1,1,0,1,1,1,1],
    7: [1,0,1,0,0,1,0],
    8: [1,1,1,1,1,1,1],
    9: [1,1,1,1,0,1,1]
}

class Segment:
    def __init__(self, channel, position, offset = 0):
        self.servo = servo.Servo(channel)
        self.position = position
        self.offset = offset
    
    def setOn(self):
        if self.position == 2 or self.position == 4:
            self.servo.angle = 110  
        else:
            self.servo.angle = 0

    def setOff(self):
        if self.position == 2 or self.position == 4:
            self.servo.angle = 0
        else:
            self.servo.angle = 110  

class Digit:
    def __init__(self, segments):
        self.segments = segments
    
    def setNumber(self, number):
        values = numberMap[number]

        for idx, segment in enumerate(self.segments):
            if values[idx] == 1:
                segment.setOn()
            else:
                segment.setOff()

    def setOff(self):
        values = [0,0,0,0,0,0,0]
        for segment in self.segments:
            segment.setOff()