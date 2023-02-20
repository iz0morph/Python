class Road:
    def __init__(self, length, width, norm_asphalt, thickness):
        self.thickness = thickness
        self.norm_asphalt = norm_asphalt
        self._length = length
        self._width = width

    def get_mass(self):
        mass = self._length * self._width * self.norm_asphalt * self.thickness
        return mass


road = Road(5000, 20, 50, 0.05)
print(f"Масса асфальта, необходимая для покрытия: {road.get_mass()}")
