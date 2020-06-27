import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7,GPIO.OUT)
pwm = GPIO.PWM(7,50)
pwm.start(5)
pwm.ChangeDutyCycle(2)
def cfa(y):
    return y/18 + 2
n = 0
while n!=200:
    n=int(input('Entert the angle '))
    pwm.ChangeDutyCycle(cfa(n))
    