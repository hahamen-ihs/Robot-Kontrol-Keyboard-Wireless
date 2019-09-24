import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
import time
GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(23, GPIO.OUT)
GPIO.setup(24, GPIO.OUT)
#import msvcrt           # import libarary keyboard
	

def maju():
    GPIO.output(14, 0)
    GPIO.output(15, 1)
    GPIO.output(23, 0)
    GPIO.output(24, 1)
def mundur():
    GPIO.output(14, 1)
    GPIO.output(15, 0)
    GPIO.output(23, 1)
    GPIO.output(24, 0)
def kiri():
    GPIO.output(14, 1)
    GPIO.output(15, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 1)
def kanan():
    GPIO.output(14, 0)
    GPIO.output(15, 1)
    GPIO.output(23, 1)
    GPIO.output(24, 0)
def stop():
    GPIO.output(14, 0)
    GPIO.output(15, 0)
    GPIO.output(23, 0)
    GPIO.output(24, 0)
try:
    while True:
        perintah = raw_input("Perintah:")
        arah = perintah[0]
        if arah == "w":
            maju()
        elif arah == "s":
            mundur()
        elif arah == "a":
            kiri()
        elif arah == "d":
            kanan()
        else:
            stop()
finally:
    print("Beres")
    GPIO.cleanup()
