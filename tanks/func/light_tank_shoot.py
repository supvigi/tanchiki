from random import randint


def light_tank_shoot(light_tank_1, heavy_tank_1, medium_tank_1):
    fire = 1
    reach_or_not = randint(1, 6)
    medium_or_heavy = int(randint(1, 2))

    if medium_or_heavy == 2:
        if reach_or_not == 1:
            heavy_tank_1.health -= light_tank_1.weapon
            light_tank_1.ammunition -= 1
            print("Reach! Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 2:
            if heavy_tank_1.armor <= 0:
                heavy_tank_1.health -= light_tank_1.weapon
                light_tank_1.ammunition -= 1
                print("Reach, but you got the armor, but the armor is broken, so you got the heavy tank itself! "
                      "Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
            else:
                heavy_tank_1.armor -= light_tank_1.weapon
                light_tank_1.ammunition -= 1
                print("Reach, but you got the armor! "
                      "Heavy tank armor:", heavy_tank_1.armor, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 3:
            heavy_tank_1.health -= light_tank_1.weapon
            heavy_tank_1.health -= fire
            light_tank_1.ammunition -= 1
            print("Reach and bonus, heavy tank is burning! "
                  "Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 4:
            heavy_tank_1.health -= light_tank_1.weapon * 2
            light_tank_1.ammunition -= 1
            print("Reach and bonus, heavy tank got critical! "
                  "Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 5:
            light_tank_1.ammunition -= 1
            print("Miss! Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 6:
            if heavy_tank_1.speed is True:
                light_tank_1.ammunition -= 1
                heavy_tank_1.speed = False
                print("Miss, heavy tank used the speed ability and dodged the bullet! "
                      "Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
            elif heavy_tank_1.speed is False:
                heavy_tank_1.health -= light_tank_1.weapon
                light_tank_1.ammunition -= 1
                print("Reach! Heavy tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        if light_tank_1.ammunition <= 0:
            print("The winner is heavy tank!")
            exit(0)
        elif heavy_tank_1.health <= 0:
            print("The winner is light tank!")
            exit(0)
        else:
            pass
    elif medium_or_heavy == 1:
        if reach_or_not == 1:
            medium_tank_1.health -= light_tank_1.weapon
            light_tank_1.ammunition -= 1
            print("Reach! Medium tank health:", heavy_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 2:
            if medium_tank_1.armor <= 0:
                medium_tank_1.health -= light_tank_1.weapon
                light_tank_1.ammunition -= 1
                print("Reach, but you got the armor, but the armor is broken, so you got the medium tank itself! "
                      "Medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
            else:
                medium_tank_1.armor -= light_tank_1.weapon
                light_tank_1.ammunition -= 1
                print("Reach, but you got the armor! "
                      "Medium tank armor:", heavy_tank_1.armor, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 3:
            medium_tank_1.health -= light_tank_1.weapon
            medium_tank_1.health -= fire
            light_tank_1.ammunition -= 1
            print("Reach and bonus, medium tank is burning! "
                  "Medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 4:
            medium_tank_1.health -= light_tank_1.weapon * 2
            light_tank_1.ammunition -= 1
            print("Reach and bonus, medium tank got critical! "
                  "Medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 5:
            light_tank_1.ammunition -= 1
            print("Miss! medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        elif reach_or_not == 6:
            if medium_tank_1.speed2 is True:
                light_tank_1.ammunition -= 1
                heavy_tank_1.speed2 = False
                print("Miss, medium tank used the speed 2 ability and dodged the bullet! "
                      "Medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
            elif medium_tank_1.speed is True:
                light_tank_1.ammunition -= 1
                medium_tank_1.speed = False
                print("Miss, medium tank used the speed ability and dodged the bullet! "
                      "Medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
            else:
                heavy_tank_1.health -= light_tank_1.weapon
                light_tank_1.ammunition -= 1
                print("Reach! Medium tank health:", medium_tank_1.health, "Light tank ammo:", light_tank_1.ammunition)
        if light_tank_1.ammunition <= 0:
            print("The winner is medium tank!")
            exit(0)
        elif medium_tank_1.health <= 0:
            print("The winner is light tank!")
            exit(0)
        else:
            pass
