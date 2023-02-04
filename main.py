class Guitars:
    def __init__(self, string: int, manufacture: int):
        """
        Создан родительский класс Guitars
        :param string: количество струн
        :param manufacture: производитель
        """
        self.__string = 0
        self.__manufacture = 0

    def get_string(self):
        """
        Создан интерфейсный метод (геттер) для возврата значения, установленного в атрибут self._sring
        :return:
        """
        return self._string

    def set_stringq(self, string, manufacture):
        if type(string) in (int) and type(manufacture) in (str):
            self.__string = string
            self.__manufacture = manufacture
        else:
            raise ValueError("Передаваемые значения должны быть типов \"int\" и \"str\"")

        """
        Создан интерфейсный метод (сеттер) для установки значения атрибуту self._sring
        :param new_string:
        :return:
        """

