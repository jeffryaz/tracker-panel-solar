from apps.orangepi.pi3 import BOARD
import OPi.GPIO as GPIO
from time import sleep
import signal
import sys
import os
from periphery import PWM

from apps.processSystem.stepperMotor import stepperULN2003

from argparse import ArgumentParser
from apps.orangepi.mg996r import MG996R
from pyA20.gpio import gpio
from pyA20.gpio import port
from pyA20.gpio import connector
import threading

start_degree = 0

# Forward rotate
stepperPIN = [3, 5, 11, 13]
# A = 3
# B = 5
# C = 11
# D = 13
# Reverse rotate
# stepperPIN = [13, 5, 11, 3]

GPIO.setwarnings(False)
GPIO.setmode(BOARD)
GPIO.setup(stepperPIN[0], GPIO.OUT)
GPIO.setup(stepperPIN[1], GPIO.OUT)
GPIO.setup(stepperPIN[2], GPIO.OUT)
GPIO.setup(stepperPIN[3], GPIO.OUT)

GPIO.output(stepperPIN[0], False)
GPIO.output(stepperPIN[1], False)
GPIO.output(stepperPIN[2], False)
GPIO.output(stepperPIN[3], False)


def index_servo_motor(sched):

    print('start')
    frequency = 50
    chipPWM = 0  # cek di /sys/class/pwm/ jika tersedia '/pwmchip8' maka chip nya 8. jika '/pwmchip0' maka chip nya 0
    pinPWM = '0'  # mengikuti chip

    try:

        # stepperULN2003(stepperPIN, 1105 * 2)

        # servo = MG996R(7, start_degree)
        # servo.move(90, 10)
        GPIO.setmode(BOARD)
        GPIO.setup(7, GPIO.OUT)
        while True:
            GPIO.output(7, GPIO.HIGH)
            # sleep(0.00001)
            GPIO.output(7, GPIO.LOW)
            # sleep(0.00001)
        GPIO.cleanup()

        # servo = GPIO.PWM(chipPWM, pinPWM, frequency, 0, False)
        # print('servo', servo)
        # servo.start_pwm()
        # servo.duty_cycle(10)
        # sleep(1)
        # servo.duty_cycle(70)
        # servo.stop_pwm()
        # GPIO.setup(7, GPIO.OUT)
        # GPIO.output(7, 0)
        # GPIO.cleanup()

    except KeyboardInterrupt:
        print("Bye.")
        GPIO.cleanup()
        # sched.shutdown(wait=False)
    # except (OSError, IOError) as e:
    #     print('e', e)
