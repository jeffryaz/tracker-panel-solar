from apps.orangepi.pi3 import BOARD
import OPi.GPIO as GPIO
from time import sleep
import signal
import sys

GPIO.setmode(BOARD)
GPIO.setup(8, GPIO.OUT)


def index_blink_light(sched):
    try:
        GPIO.output(8, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(8, GPIO.LOW)
        sleep(0.5)

        GPIO.output(8, GPIO.HIGH)
        sleep(0.5)
        GPIO.output(8, GPIO.LOW)

    except KeyboardInterrupt:
        GPIO.output(8, GPIO.LOW)
        GPIO.cleanup()
        sched.shutdown(wait=False)
        print("Bye.")
