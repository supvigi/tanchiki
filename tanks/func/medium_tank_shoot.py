from random import randint


def medium_tank_shoot(light_tank_1, heavy_tank_1, medium_tank_1):
    fire = 1
    reach_or_not = randint(1, 7)
    light_or_heavy = int(randint(1, 2))

    if light_or_heavy == 1:
        if reach_or_not == 1:
            heavy_tank_1.health -= medium_tank_1.weapon
            medium_tank_1.ammunition -= 1
            print("Reach! Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 2:
            if heavy_tank_1.armor <= 0:
                heavy_tank_1.health -= medium_tank_1.weapon
                medium_tank_1.ammunition -= 1
                print("Reach, but you got the armor, but the armor is broken, so you got the heavy tank itself! "
                      "Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
            else:
                heavy_tank_1.armor -= medium_tank_1.weapon
                medium_tank_1.ammunition -= 1
                print("Reach, but you got the armor! "
                      "Heavy tank armor:", heavy_tank_1.armor, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 3:
            heavy_tank_1.health -= medium_tank_1.weapon
            heavy_tank_1.health -= fire
            medium_tank_1.ammunition -= 1
            print("Reach and bonus, heavy tank is burning! "
                  "Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 4:
            heavy_tank_1.health -= medium_tank_1.weapon * 2
            medium_tank_1.ammunition -= 1
            print("Reach and bonus, Tank 1 got critical! "
                  "Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 5:
            medium_tank_1.ammunition -= 1
            print("Miss! Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 6:
            if heavy_tank_1.speed is True:
                medium_tank_1.ammunition -= 1
                heavy_tank_1.speed = False
                print("Miss, heavy tank used the speed ability and dodged the bullet! "
                      "Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
            else:
                heavy_tank_1.health -= medium_tank_1.weapon
                medium_tank_1.ammunition -= 1
                print("Reach! Heavy tank health:", heavy_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        if medium_tank_1.ammunition <= 0:
            print("The winner is heavy tank!")
            exit(0)
        elif heavy_tank_1.health <= 0:
            print("The winner is medium tank!")
            exit(0)
        else:
            pass
    if light_or_heavy == 2:
        if reach_or_not == 1:
            light_tank_1.health -= medium_tank_1.weapon
            medium_tank_1.ammunition -= 1
            print("Reach! Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 2:
            if light_tank_1.armor <= 0:
                light_tank_1.health -= medium_tank_1.weapon
                medium_tank_1.ammunition -= 1
                print("Reach, but you got the armor, but the armor is broken, so you got the light tank itself! "
                      "Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
            else:
                light_tank_1.armor -= medium_tank_1.weapon
                medium_tank_1.ammunition -= 1
                print("Reach, but you got the armor! "
                      "Light tank armor:", light_tank_1.armor, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 3:
            light_tank_1.health -= medium_tank_1.weapon
            light_tank_1.health -= fire
            medium_tank_1.ammunition -= 1
            print("Reach and bonus, light tank is burning! "
                  "Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 4:
            light_tank_1.health -= medium_tank_1.weapon * 2
            medium_tank_1.ammunition -= 1
            print("Reach and bonus, Tank 1 got critical! "
                  "Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 5:
            medium_tank_1.ammunition -= 1
            print("Miss! Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 6:
            if light_tank_1.speed is True:
                medium_tank_1.ammunition -= 1
                light_tank_1.speed = False
                print("Miss, light tank used the speed ability and dodged the bullet! "
                      "Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
            else:
                light_tank_1.health -= medium_tank_1.weapon
                medium_tank_1.ammunition -= 1
                print("Reach! Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        elif reach_or_not == 7:
            medium_tank_1.ammunition -= 1
            print("Miss, light tank used the miss ability and dodged the bullet! "
                  "Light tank health:", light_tank_1.health, "Medium tank ammo:", medium_tank_1.ammunition)
        if medium_tank_1.ammunition <= 0:
            print("The winner is light tank!")
            exit(0)
        elif light_tank_1.health <= 0:
            print("The winner is medium tank!")
            exit(0)
        else:
            pass
