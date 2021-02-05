from tanks.func.light_tank_shoot import light_tank_shoot
from tanks.func.medium_tank_shoot import medium_tank_shoot
from tanks.func.heavy_tank_shoot import heavy_tank_shoot
from tanks.cls.heavy_tank import HeavyTank
from tanks.cls.medium_tank import MediumTank
from tanks.cls.light_tank import LightTank
from tanks.data.settings import *


def run():
    lst = []
    for i in range(PLAYER_QTY):
        tank = input("Light tank = 1\nMedium tank = 2\nHeavy tank = 3\nSelect the tank. "
                     "If you put in \"stop\" program will stop adding players: ")
        if tank == "stop" or "Stop":
            break

        if tank == "1":
            lst.append(LightTank(LIGHT_TANK_ARGS))
            if i == 1:
                player1 = lst[0]
            elif i == 2:
                player2 = lst[1]
            else:
                player3 = lst[2]
            print("You selected the light tank")
        elif tank == "2":
            lst.append(MediumTank(MEDIUM_TANK_ARGS))
            if i == 1:
                player1 = lst[0]
            elif i == 2:
                player2 = lst[1]
            else:
                player3 = lst[2]
            print("You selected the medium tank")
        elif tank == "3":
            lst.append(HeavyTank(HEAVY_TANK_ARGS))
            if i == 1:
                player1 = lst[0]
            elif i == 2:
                player2 = lst[1]
            else:
                player3 = lst[2]
            print("You selected the heavy tank")

    while True:
        move = input("Put in who shoots: ")
        if move == "player1 shoot"