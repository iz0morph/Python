class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_mass(self, norm_asphalt, thickness):
        mass = self._length * self._width * norm_asphalt * thickness
        return mass


road = Road(5000, 20)
print(f"Масса асфальта, необходимая для покрытия: {road.get_mass(25, 0.05)}")
