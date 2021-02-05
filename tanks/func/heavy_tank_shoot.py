from random import randint


def heavy_tank_shoot(light_tank_1, heavy_tank_1, medium_tank_1):
    fire = 1
    reach_or_not = randint(1, 8)
    medium_or_light = int(randint(1, 2))

    if medium_or_light == 1:
        if reach_or_not == 1:
            light_tank_1.health -= heavy_tank_1.weapon
            heavy_tank_1.ammunition -= 1
            print("Reach! Light tank health:", light_tank_1.health, "Light tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 2:
            if light_tank_1.armor <= 0:
                light_tank_1.health -= heavy_tank_1.weapon
                heavy_tank_1.ammunition -= 1
                print("Reach, but you got the armor, but the armor is broken, so you got the light tank itself! "
                      "Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
            else:
                light_tank_1.armor -= heavy_tank_1.weapon
                heavy_tank_1.ammunition -= 1
                print("Reach, but you got the armor! "
                      "Light tank armor:", light_tank_1.armor, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 3:
            light_tank_1.health -= heavy_tank_1.weapon
            light_tank_1.health -= fire
            heavy_tank_1.ammunition -= 1
            print("Reach and bonus, light tank is burning! "
                  "Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 4:
            light_tank_1.health -= heavy_tank_1.weapon * 2
            heavy_tank_1.ammunition -= 1
            print("Reach and bonus, light tank got critical! "
                  "Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 5:
            heavy_tank_1.ammunition -= 1
            print("Miss! Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 6:
            if light_tank_1.speed is True:
                heavy_tank_1.ammunition -= 1
                light_tank_1.speed = False
                print("Miss, light tank used the speed ability and dodged the bullet! "
                      "Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
            elif light_tank_1.speed is False:
                light_tank_1.health -= heavy_tank_1.weapon
                heavy_tank_1.ammunition -= 1
                print("Reach! Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 7:
            heavy_tank_1.ammunition -= 1
            print("Miss! Light tank used the miss ability and dodged the bullet! "
                  "Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 8:
            light_tank_1.health -= heavy_tank_1.weapon2
            heavy_tank_1.ammunition -= 1
            print("Reach, heavy tank used the reach ability and hit the light tank! "
                  "Light tank health:", light_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        if heavy_tank_1.ammunition <= 0:
            print("The winner is light tank!")
            exit(0)
        elif light_tank_1.health <= 0:
            print("The winner is heavy tank!")
            exit(0)
        else:
            pass
    if medium_or_light == 2:
        if reach_or_not == 1:
            medium_tank_1.health -= heavy_tank_1.weapon
            heavy_tank_1.ammunition -= 1
            print("Reach! Medium tank health:", medium_tank_1.health, "Light tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 2:
            if medium_tank_1.armor <= 0:
                medium_tank_1.health -= heavy_tank_1.weapon
                heavy_tank_1.ammunition -= 1
                print("Reach, but you got the armor, but the armor is broken, so you got the medium tank itself! "
                      "Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
            else:
                medium_tank_1.armor -= heavy_tank_1.weapon
                heavy_tank_1.ammunition -= 1
                print("Reach, but you got the armor! "
                      "Medium tank armor:", medium_tank_1.armor, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 3:
            medium_tank_1.health -= heavy_tank_1.weapon
            medium_tank_1.health -= fire
            heavy_tank_1.ammunition -= 1
            print("Reach and bonus, medium tank is burning! "
                  "Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 4:
            medium_tank_1.health -= heavy_tank_1.weapon * 2
            heavy_tank_1.ammunition -= 1
            print("Reach and bonus, medium tank got critical! "
                  "Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 5:
            heavy_tank_1.ammunition -= 1
            print("Miss! Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 6:
            if medium_tank_1.speed is True:
                heavy_tank_1.ammunition -= 1
                medium_tank_1.speed = False
                print("Miss, medium tank used the speed ability and dodged the bullet! "
                      "Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
            elif medium_tank_1.speed2 is True:
                heavy_tank_1.ammunition -= 1
                print("Miss, medium tank used the speed 2 ability and dodged the bullet! "
                      "Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
            else:
                medium_tank_1.health -= heavy_tank_1.weapon
                heavy_tank_1.ammunition -= 1
                print("Reach! Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        elif reach_or_not == 7:
            medium_tank_1.health -= heavy_tank_1.weapon2
            heavy_tank_1.ammunition -= 1
            print("Reach, heavy tank used the reach ability an hit the medium tank! "
                  "Medium tank health:", medium_tank_1.health, "Heavy tank ammo:", heavy_tank_1.ammunition)
        if heavy_tank_1.ammunition <= 0:
            print("The winner is light tank!")
            exit(0)
        elif light_tank_1.health <= 0:
            print("The winner is heavy tank!")
            exit(0)
        else:
            pass
