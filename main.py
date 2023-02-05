import random

COLORS = ['dark', 'blue', 'yellow', 'purple', 'white']


class Guitars:
    def __init__(self, string: int, manufacture: (int, str)):
        """
        Создан родительский класс Guitars
        :param string: количество струн
        :param manufacture: производитель
        """
        self.__string = 0
        self.__manufacture = 0
        if self.__test(string) and self.__test(manufacture):
            self.__string = string
            self.__manufacture = manufacture

    @classmethod
    def __test(cls, string):
        return type(string) in (int, str)

    @property
    def get_string(self):
        """
        Создан интерфейсный метод (геттер) для возврата значения, установленного в атрибут self._sring
        :return:
        """
        return self.__string

    @get_string.setter
    def get_string(self, string):
        if self.__test(string):
            self.__string = string
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._sring
        :param new_string:
        :return:
        """

    @get_string.deleter
    def get_string(self):
        del self.__string

    @property
    def manufacture(self):
        """
        Создан интерфейсный метод (геттер) для возврата значения, установленного в атрибут self._manufacture
        :return:
        """
        return self.__manufacture

    @manufacture.setter
    def manufacture(self, manufacture):
        if self.__test(manufacture):
            self.__string = manufacture
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._manufacture
        :param new_string:
        :return:
        """

    @manufacture.deleter
    def manufacture(self):
        del self.__manufacture

    def paint_guitar(self):
        random_color = random.randint(0, len(COLORS) - 1)
        return COLORS[random_color]

    def __str__(self):
        return f"Количество струн = {self.__string}, Производитель гитары - {self.manufacture}"

    def __repr__(self):
        return f"{self.__class__}: {self.__string!r}, {self.__manufacture!r}"


class Electric_guitars(Guitars):
    """
    Электрогитары - дочерний класс
    """

    def __init__(self, string: int, manufacture: (int, str)):
        super().__init__(string, manufacture)
        self.model = "Stratocaster"

    @property
    def model(self) -> str:
        """
        Создан геттер
        :return: Должен вернуть модель электрогитары
        """
        return self.model

    @model.setter
    def model(self, new_model) -> None:
        self.model = new_model


c = Guitars(6, 'Fender')
c.get_string = 9
print(c.get_string)
