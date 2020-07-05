import socket, traceback
import re
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
#7 is up down
pwm1 = GPIO.PWM(7,50)
pwm2 = GPIO.PWM(5,50)
pwm1.start(5)
pwm1.ChangeDutyCycle(2)

pwm2.start(5)
pwm2.ChangeDutyCycle(7)
angle = 90
vals = {
    9:0,
    8:20,
    7:20,
    6:40,
    5:40,
    4:60,
    3:60,
    2:80,
    1:80,
    0:100,
    -1:100,
    -2:120,
    -3:120,
    -4:140,
    -5:140,
    -6:160,
    -7:160,
    -8:180,
    -9:180
}
host = ''
port = 5555
n = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
n.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
n.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
n.bind((host, port))


def cfa(y):
    return y/18 + 2



def servomove2(dd):
    pwm2.ChangeDutyCycle(cfa(int(float(dd))))


def motor1(d):
    #print(vals[int(float(d))])
    pwm1.ChangeDutyCycle(cfa(vals[int(float(d))]))

def motor2(d):
    global angle
    if angle >= 0 and angle <= 180 and abs(int(float(d))) >0  :
        angle +=  int(float(d))
        if angle>180:
            angle = 180
        elif angle <0:
            angle = 0
    #print(str(int(angle)) + ' ' + str(y))
    servomove2(angle)


while 1:
    try:
        message, address = n.recvfrom(8192)
        message = str(message)
        if len(message) > 8:
            message = re.findall(r'[^,\s][^\,]*[^,\s]*',message)
            yeeet = re.sub(r'\'','',message[6])
            yeet = re.sub(r'\'','',message[4])
            motor1 (yeet)
            motor2 (yeeet)

    except (KeyboardInterrupt, SystemExit):
        raise
    except:
        traceback.print_exc()


