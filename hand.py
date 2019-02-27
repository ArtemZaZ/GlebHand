import xmlrpc.client
import joystick
from config import *
import time

proxy = "http://" + IP + ':' + PORT

J = joystick.Joystick()
J.open("/dev/input/js0")
J.start()
print(J)

client = xmlrpc.client.ServerProxy(proxy)

f1 = 0.0    # глобальные переменные для 5 пальцев
f2 = 0.0
f3 = 0.0
f4 = 0.0
f5 = 0.0


def rerange(f):     # если перегоняет диапазон, вгоняем его в  (0, 1)
    if f >= 1.0:
        return 1.0
    elif f <= 0.0:
        return 0.0
    else:
        return f


while True:
    if J.buttons[FINGER_1_BUTTON]:
        f1 = f1 + FINGER_SCALE_STEP
    else:
        f1 = f1 - FINGER_SCALE_STEP
    f1 = rerange(f1)

    if J.buttons[FINGER_2_BUTTON]:
        f2 = f2 + FINGER_SCALE_STEP
    else:
        f2 = f2 - FINGER_SCALE_STEP
    f2 = rerange(f2)

    if J.buttons[FINGER_3_BUTTON]:
        f3 = f3 + FINGER_SCALE_STEP
    else:
        f3 = f3 - FINGER_SCALE_STEP
    f3 = rerange(f3)

    if J.buttons[FINGER_4_BUTTON]:
        f4 = f4 + FINGER_SCALE_STEP
    else:
        f4 = f4 - FINGER_SCALE_STEP
    f4 = rerange(f4)

    if J.buttons[FINGER_5_BUTTON]:
        f5 = f5 + FINGER_SCALE_STEP
    else:
        f5 = f5 - FINGER_SCALE_STEP
    f5 = rerange(f5)

    client.bendFinger(1, f1)
    client.bendFinger(2, f2)
    client.bendFinger(3, f3)
    client.bendFinger(4, f4)
    client.bendFinger(5, f5)
    time.sleep(SEND_DELAY)
