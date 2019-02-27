import xmlrpc.client
import joystick
from config import *
import time

proxy = "http://" + IP + ':' + PORT

J = joystick.Joystick()
J.open("/dev/input/js0")
print(J)

client = xmlrpc.client.ServerProxy(proxy)

f1 = 0.0    # глобальные переменные для 5 пальцев
f2 = 0.0
f3 = 0.0
f4 = 0.0
f5 = 0.0


while True:
    if J.buttons[FINGER_1_BUTTON]:
        f1 = f1 + FINGER_SCALE_STEP
    else:
        f1 = f1 - FINGER_SCALE_STEP

    if J.buttons[FINGER_2_BUTTON]:
        f2 = f2 + FINGER_SCALE_STEP
    else:
        f2 = f2 - FINGER_SCALE_STEP

    if J.buttons[FINGER_3_BUTTON]:
        f3 = f3 + FINGER_SCALE_STEP
    else:
        f3 = f3 - FINGER_SCALE_STEP

    if J.buttons[FINGER_4_BUTTON]:
        f4 = f4 + FINGER_SCALE_STEP
    else:
        f4 = f4 - FINGER_SCALE_STEP

    if J.buttons[FINGER_5_BUTTON]:
        f5 = f5 + FINGER_SCALE_STEP
    else:
        f5 = f5 - FINGER_SCALE_STEP

    client.bendFinger(1, f1)
    client.bendFinger(2, f2)
    client.bendFinger(3, f3)
    client.bendFinger(4, f4)
    client.bendFinger(5, f5)
    time.sleep(SEND_DELAY)
