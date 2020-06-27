import curses
import RPi.GPIO as GPIO


def forward():
    GPIO.output(3,1)
    GPIO.output(5,0)
    GPIO.output(8,1)
    GPIO.output(10,0)

def backwards():
    GPIO.output(3,0)
    GPIO.output(5,1)
    GPIO.output(8,0)
    GPIO.output(10,1)

def left():
    GPIO.output(3,1)
    GPIO.output(5,0)
    GPIO.output(8,0)
    GPIO.output(10,1)

def right():
    GPIO.output(3,0)
    GPIO.output(5,1)
    GPIO.output(8,1)
    GPIO.output(10,0)

def stop():
    GPIO.output(3,0)
    GPIO.output(5,0)
    GPIO.output(8,0)
    GPIO.output(10,0)

GPIO.setmode(GPIO.BOARD)
GPIO.setup(3,GPIO.OUT)
GPIO.setup(5,GPIO.OUT)
GPIO.setup(8,GPIO.OUT)
GPIO.setup(10,GPIO.OUT)


def main(stdscr):
    stdscr.nodelay(1)
    while True:
        c = stdscr.getch()
        #up arrow is 259
        #down 258
        #left 260
        #right 261
        if c != -1:
            if c == 259:
                print('forward')
                forward()
            if c == 258:
                print('Backwards')
                backwards()
            if c == 260:
                print('left')
                left()
            if c == 261:
                print('right')
                right()
            stop()
        else:
            stop()
            print('stop')

if __name__ == '__main__':
    curses.wrapper(main)