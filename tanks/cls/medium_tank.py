from tanks.cls.tank import Tank


class MediumTank(Tank):
    def __init__(self, args):
        super().__init__(args["wp"], args["arm"], args["hp"], args["ammo"], args["spd"])
        self.speed2 = args["spd2"]
