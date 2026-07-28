class Tire:
    def __init__(self, traction_coef, vertical_load):

        self.traction_coef = traction_coef
        self.vertical_load = vertical_load

    def get_max_grip(self):

        max_grip = self.vertical_load * self.traction_coef

        return max_grip