class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def calc_mass(self):
        calc_mass = self._length * self._width * self.weight * self.height / 1000
        print(f'Для покрытия всей дороги необходимо {round(calc_mass)} массы асфальта')


r = Road(5000, 20)
r.calc_mass()