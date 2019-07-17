import sys
import math
from adafruit_servokit import ServoKit

# UPDATE: camera view values
image_width = 3000
image_height = 2000
camera_position = image_width / 2;

def determine_angle(raw_x, raw_y):
    y = image_height - raw_y
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
    if len(sys.argv) == 3:
        kit = ServoKit(channels=8) #init
        x = int(sys.argv[1])
        y = int(sys.argv[2])

        angle = determine_angle(x, y)
        move_servo(int(round(angle)))

    else:
        print('needs (x,y) coordinates')
        print('> python3 script.py <x_value> <y_value>')
