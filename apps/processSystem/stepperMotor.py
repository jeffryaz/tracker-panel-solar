from apps.orangepi.pi3 import BOARD
import OPi.GPIO as GPIO
from time import sleep


def stepperULN2003(stepperPIN, rotate=1):
    try:
        GPIO.setmode(BOARD)
        GPIO.setwarnings(False)
        pins = stepperPIN
        latency = 0.01
        # latency = 0.05

        # [A,B,D,C]
        # full-step plus half-step (step in cycle, pin output)
        sequence = [[1, 1, 1, 0],
                    [0, 1, 1, 1]]

        # 1 Putaran 2150 dengan latency = 0.01
        # step(n=2150)
        # full-step (step in cycle, pin output)
        # sequence = [[1, 1, 0, 0],
        #             [0, 1, 1, 0],
        #             [0, 0, 1, 1],
        #             [1, 0, 0, 1]]

        # half-step (step in cycle, pin output)
        # sequence = [[1, 0, 0, 0],
        #             [1, 1, 0, 0],
        #             [0, 1, 0, 0],
        #             [0, 1, 1, 0],
        #             [0, 0, 1, 0],
        #             [0, 0, 1, 1],
        #             [0, 0, 0, 1],
        #             [1, 0, 0, 1]]

        for x in stepperPIN:
            GPIO.setup(x, GPIO.OUT)

        def read_pins():
            config = []
            for p in range(len(pins)):
                config.append(GPIO.input(pins[p]))
            return config

        def cycle(sequence):
            for i in range(len(sequence)):
                for p in range(len(pins)):
                    GPIO.output(pins[p], sequence[i][p])
                sleep(latency)
            return None

        def step(n=1):
            sequences = sequence

            sign = n/abs(n)
            if sign < 0:
                sequences = sequences[::-1]
            n = abs(n)

            config = read_pins()
            cycle_index = len(sequences) - 1

            for i in range(len(sequences)):
                if config == sequences[i]:
                    cycle_index = i

            n_before = max(0, min(n, len(sequences) - cycle_index - 1))
            n_after = (n - n_before) % len(sequences)
            n_cycles = (n-n_before-n_after)//len(sequences)

            for j in range(n_before):
                for p in range(len(pins)):
                    GPIO.output(pins[p], sequence[cycle_index+j+1][p])
                sleep(latency)

            for k in range(n_cycles):
                cycle(sequence)

            for l in range(n_after):
                for p in range(len(pins)):
                    GPIO.output(pins[p], sequence[l][p])
                sleep(latency)

            return None
        # 1 Putaran 1030 dengan latency = 0.01
        step(n=rotate)

        GPIO.output(stepperPIN[0], False)
        GPIO.output(stepperPIN[1], False)
        GPIO.output(stepperPIN[2], False)
        GPIO.output(stepperPIN[3], False)

    except KeyboardInterrupt:
        print("Bye.")
        GPIO.cleanup()
        # sched.shutdown(wait=False)
    except (OSError, IOError) as e:
        print('e', e)
