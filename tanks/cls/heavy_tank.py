from tanks.cls.tank import Tank


class HeavyTank(Tank):
    def __init__(self, args):
        super().__init__(args["wp"], args["arm"], args["hp"], args["ammo"], args["spd"])
        self.weapon2 = args["wp2"]
