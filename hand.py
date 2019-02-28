import xmlrpc.client
from config import *
import time
from pynput.keyboard import Key, Listener, KeyCode
import threading

proxy = "http://" + IP + ':' + PORT

client = xmlrpc.client.ServerProxy(proxy)

finger1 = 0.0  # глобальные переменные для 5 пальцев
finger2 = 0.0
finger3 = 0.0
finger4 = 0.0
finger5 = 0.0

fingerKeyState1 = False     # состояния клавиш
fingerKeyState2 = False
fingerKeyState3 = False
fingerKeyState4 = False
fingerKeyState5 = False


def on_press(key):
    global fingerKeyState1
    global fingerKeyState2
    global fingerKeyState3
    global fingerKeyState4
    global fingerKeyState5
    if key == KeyCode.from_char('1'):
        fingerKeyState1 = True
    elif key == KeyCode.from_char('2'):
        fingerKeyState2 = True
    elif key == KeyCode.from_char('3'):
        fingerKeyState3 = True
    elif key == KeyCode.from_char('4'):
        fingerKeyState4 = True
    elif key == KeyCode.from_char('5'):
        fingerKeyState5 = True


def on_release(key):
    global fingerKeyState1
    global fingerKeyState2
    global fingerKeyState3
    global fingerKeyState4
    global fingerKeyState5
    if key == KeyCode.from_char('1'):
        fingerKeyState1 = False
    elif key == KeyCode.from_char('2'):
        fingerKeyState2 = False
    elif key == KeyCode.from_char('3'):
        fingerKeyState3 = False
    elif key == KeyCode.from_char('4'):
        fingerKeyState4 = False
    elif key == KeyCode.from_char('5'):
        fingerKeyState5 = False
    elif key == Key.esc:
        # Stop listener
        return False


def rerange(f):     # если перегоняет диапазон, вгоняем его в  (0, 1)
    if f >= 1.0:
        return 1.0
    elif f <= 0.0:
        return 0.0
    else:
        return f


def threadFunc():
    # Collect events until released
    with Listener(
            on_press=on_press,
            on_release=on_release) as listener:
        listener.join()


threading.Thread(target=threadFunc).start()


while True:
    if fingerKeyState1:
        finger1 = finger1 + FINGER_SCALE_STEP
    else:
        finger1 = finger1 - FINGER_SCALE_STEP
    finger1 = rerange(finger1)

    if fingerKeyState2:
        finger2 = finger2 + FINGER_SCALE_STEP
    else:
        finger2 = finger2 - FINGER_SCALE_STEP
    finger2 = rerange(finger2)

    if fingerKeyState3:
        finger3 = finger3 + FINGER_SCALE_STEP
    else:
        finger3 = finger3 - FINGER_SCALE_STEP
    finger3 = rerange(finger3)

    if fingerKeyState4:
        finger4 = finger4 + FINGER_SCALE_STEP
    else:
        finger4 = finger4 - FINGER_SCALE_STEP
    finger4 = rerange(finger4)

    if fingerKeyState5:
        finger5 = finger5 + FINGER_SCALE_STEP
    else:
        finger5 = finger5 - FINGER_SCALE_STEP
    finger5 = rerange(finger5)
    client.bendFinger(1, finger1)
    client.bendFinger(2, finger2)
    client.bendFinger(3, finger3)
    client.bendFinger(4, finger4)
    client.bendFinger(5, finger5)
    time.sleep(SEND_DELAY)

