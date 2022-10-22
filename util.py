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

# Some fine tuning on the digit positioning
digitOffsetMap = {
    "hours": {
        "digitOne": {
            0: 5,
            1: -5,
            2: 5,
            3: -5,
            4: 5,
            5: -3,
            6: -3,
        },
        "digitTwo": {
            8: 0,
            9: 5,
            10: 8,
            11: -8,
            12: 0,
            13: 0,
            14: -5,
        }
    },
    "minutes": {
        "digitOne": {
                0: 10,
                1: -10,
                2: 0,
                3: 5,
                4: 0,
                5: -10,
                6: 10,
            },
        "digitTwo": {
                8: 10,
                9: -13,
                10: 13,
                11: 0,
                12: 10,
                13: -5,
                14: 0,
            }
    },
}


class Segment:
    def __init__(self, channel, position, offset = 0):
        self.servo = servo.Servo(channel)

        if position == 2 or position == 4:
            self.onAngle = 130 + offset
            self.offAngle = 20 + offset
        else:
            self.onAngle = 20 + offset
            self.offAngle = 130 + offset
        
    def setOn(self):
        self.servo.angle = self.onAngle

    def setOff(self):
        self.servo.angle = self.offAngle

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
        for segment in self.segments:
            segment.setOff()