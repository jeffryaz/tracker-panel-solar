from apps.orangepi.pi3 import BOARD
import OPi.GPIO as GPIO
from time import sleep
import signal
import sys


def index_blink_light():
    GPIO.setmode(BOARD)
    GPIO.setup(8, GPIO.OUT)
    # try:
    #     while True:
    GPIO.output(8, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(8, GPIO.LOW)
    sleep(0.5)

    GPIO.output(8, GPIO.HIGH)
    sleep(0.5)
    GPIO.output(8, GPIO.LOW)

    # except KeyboardInterrupt:
    #     GPIO.output(8, GPIO.LOW)
    GPIO.cleanup()
    #     print("Bye.")
