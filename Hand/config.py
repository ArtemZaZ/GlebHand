""" Конфигурация руки """
from RPiPWM import *

IP = '192.168.42.11'   # ip адрес ПК
PORT = 8000

chanSrvF1 = 6   # каналы серв пальцев
chanSrvF2 = 7
chanSrvF3 = 8
chanSrvF4 = 9
chanSrvF5 = 10

scaleFactor = 180     # разрешение сервы в градусах

SvrF1 = Servo180(chanSrvF1)
SvrF2 = Servo180(chanSrvF2)
SvrF3 = Servo180(chanSrvF3)
SvrF4 = Servo180(chanSrvF4)
SvrF5 = Servo180(chanSrvF5)


def bendFinger(num, scale):     # num - номер, scale - величина изгиба [0, 1]
    if num == 1:
        SvrF1.SetValue(scale * scaleFactor)
    elif num == 2:
        SvrF2.SetValue(scale * scaleFactor)
    elif num == 3:
        SvrF3.SetValue(scale * scaleFactor)
    elif num == 4:
        SvrF4.SetValue(scale * scaleFactor)
    elif num == 5:
        SvrF5.SetValue(scale * scaleFactor)
    else:
        return False
    return True

