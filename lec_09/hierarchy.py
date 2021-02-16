class Base:
    def __init__(self, x) -> None:
        self.x = x

    def show(self):
        print('Base', self.x)


class Derivative(Base):
    def __init__(self, x) -> None:
        super().__init__(x) # явный вызов конструктора Python
        self.name = ''


a = Base('base')
b = Derivative('derivative')

a.show()
b.show()