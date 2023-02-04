class Guitars:
    def __init__(self, string: [int] = None, manufacture: [str] = None):
        """
        Создан родительский класс Guitars
        :param string: количество струн
        :param manufacture: производитель
        """
        self._string = None
        self.manufacture = None

    @property
    def stringw(self):
        return self._string

    @stringw.setter
    def stringw(self, new_string):
        if (new_string < 1):
            raise ValueError("Количество струн не может быть меньше одной")
        print("Это сеттер метод")
        self._string = new_string
