from tanks.cls.tank import Tank


class LightTank(Tank):
    def __init__(self, args):
        super().__init__(args["wp"], args["arm"], args["hp"], args["ammo"], args["spd"])
        self.miss = args["miss"]
