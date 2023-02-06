# from apps.processSystem.blinkLight import index_blink_light
from apps.processSystem.servoMotor import index_servo_motor


def register_process(sched):
    # index_blink_light(sched)
    index_servo_motor(sched)
