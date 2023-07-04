
import time


class My_str(str):
    """
    Расширяемый класс str, где:
    доступны все возможности str.
    """

    def __new__(cls, value: str, name: str):
        """
        Расширяемый метод, в котором дополнительно хранятся имя автора строки и время создания (time.time)
        :param value:
        :param name:
        """
        instance = super().__new__(cls, value)
        instance.name = name
        instance.created_at = time.time()
        return instance

    def __str__(self):
        return f'автор {self.name}, создано {self.created_at}'

    def __repr__(self):
        return f'автор {self.name = }, создано {self.created_at = }'


item1 = My_str('строка', "Oleg")
print(item1.name, item1.created_at)
print(item1)
print(repr(item1))