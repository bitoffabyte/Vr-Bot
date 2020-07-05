import socket, traceback
import re
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
pwm = GPIO.PWM(7,50)
pwm.start(5)
pwm.ChangeDutyCycle(2)
angle = 90

host = ''
port = 5555
n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
n.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
n.bind((host, port))
def cfa(y):
    return y/18 + 2
def servomove(dd):
    pwm.ChangeDutyCycle(cfa(int(float(dd))))
def yeet(d):
    global angle
    if angle >= 0 and angle <= 180:
        angle +=  int(float(d))/5
        if angle>180:
            angle = 180
        elif angle <0:
            angle = 0
    print(str(int(angle)) + ' ' + str(int(float(d))))
    servomove(int(float(angle)))

while 1:
    try:
        message, address = n.recvfrom(8192)
        message = str(message)
        if len(message) > 8:
            message = re.findall(r'[^,\s][^\,]*[^,\s]*',message)
            yeeet = re.sub(r'\'','',message[6])
            yeet (yeeet)

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()

