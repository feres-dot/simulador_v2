class Tire:
    def __init__(self, traction_coef, vertical_load):

        self.traction_coef = traction_coef
        self.vertical_load = vertical_load

    def get_max_grip(self):

        max_grip = self.vertical_load * self.traction_coef

        return max_grip

    #Method to get the updated load depending on the load transfer

    def update_load(self, new_load):
        self.vertical_load = new_load
