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

start_degree = 360
state_file = '.servo-state'

# Forward rotate
stepperPIN = [3, 5, 11, 13]
# A = 3
# B = 5
# C = 11
# D = 13
# Reverse rotate
# stepperPIN = [13, 5, 11, 3]

GPIO.setmode(BOARD)
GPIO.setwarnings(False)
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
    frequency = 0.05
    chipPWM = 0  # cek di /sys/class/pwm/ jika tersedia '/pwmchip8' maka chip nya 8. jika '/pwmchip0' maka chip nya 0
    pinPWM = 0  # mengikuti chip

    try:
        # stepperULN2003(stepperPIN, 1105 * 2)
        # GPIO.cleanup()

        # servo = GPIO.PWM(chipPWM, pinPWM, frequency, 0, False)
        # duty = 1
        # while duty <= 17:
        #     servo.duty_cycle(duty)
        #     sleep(1)
        #     duty = duty + 1
        # servo.duty_cycle(100)
        # servo.start_pwm()
        # sleep(1)
        # servo.stop_pwm()

        # pwm = PWM(0, 0)
        # pwm.duty_cycle = 0
        # pwm.frequency = 5000
        # pwm.enable()
        # pwm.duty_cycle = 1
        # pwm.frequency = 5500
        # pwm.close()
        # GPIO.cleanup()

        servo = MG996R('7', 360)
        servo.move(120)
        # with open(state_file, 'w') as f:
        #     f.write(str(args.deg))

        

    except KeyboardInterrupt:
        print("Bye.")
        GPIO.cleanup()
        # sched.shutdown(wait=False)
    # except (OSError, IOError) as e:
    #     print('e', e)
