import sys
import math
from adafruit_servokit import ServoKit

# camera view values
image_width = 3000
camera_position = image_width / 2;

def determine_angle(raw_x, y):
    if raw_x <= camera_position:
        x = camera_position - raw_x
        angle = 180 - math.degrees(math.atan(y/x))
    elif raw_x > camera_position:
        x = raw_x - camera_position
        angle = math.degrees(math.atan(y/x))
    return angle

def move_servo(angle):
    kit.servo[0].angle = angle

if __name__ == '__main__':
    # through command line
    # python script.py <x_value> <y_value>
    if len(sys.argv) == 3:
        kit = ServoKit(channels=8) #init
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        angle = determine_angle(x, y)
        move_servo(int(round(angle)))

    else:
        print('needs (x,y) coordinates')
        print('> python script.py <x_value> <y_value>')
