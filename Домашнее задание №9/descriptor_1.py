class Validation:
    def __set__(self, instance, value):
        if type(value) not in (int, float):
            raise TypeError(f'{self.my_attr} не является числом!')
        elif value <= 0:
            raise ValueError(f'{self.my_attr} должен быть положительным!')
        instance.__dict__[self.my_attr] = value

    def __set_name__(self, owner, my_attr):
        self.my_attr = my_attr



class Road:
    thickness=Validation()
    norm_asphalt=Validation()
    _length=Validation()
    _width=Validation()
    def __init__(self, length, width, norm_asphalt, thickness):
        self.thickness = thickness
        self.norm_asphalt = norm_asphalt
        self._length = length
        self._width = width

    def get_mass(self):
        mass = self._length * self._width * self.norm_asphalt * self.thickness
        return mass


road = Road(5000, -20, 50, 0.05)
print(f"Масса асфальта, необходимая для покрытия: {road.get_mass()}")