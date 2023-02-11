import logging

from time import sleep
from apps.orangepi.orangepwm import OrangePwm


class MG996R:
    def __init__(self, pin: str, prev: int = 360):
        self.pwm = OrangePwm(50, pin)
        self.prev = prev

        logging.debug(
            f'Initialized MG996R class with starting degree of {prev}')

    def move(self, deg, delay: int = 0):
        distance = abs(self.prev - deg)
        sleep_time = distance / 60 * .5 + delay

        duty = deg / 18 + 2
        logging.debug(
            f'Moving to {deg} degrees, duty {duty:.0f}%, sleeping for {sleep_time:.1f} sec.')

        self.prev = deg

        self.pwm.start(duty)
        sleep(sleep_time + delay)
        self.pwm.stop()
