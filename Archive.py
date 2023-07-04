class Archive:
    """
    Класс Архив хранит пару свойств.
    число и строку.
    """
    numbers = []
    values = []


    def __new__(cls, number: int, value: str):
        """
        При создании нового экземпляра класса, старые данные из ранее
        созданных экземпляров сохраняются в пару списков архивов
        list-архивы также являются свойствами экземпляра
        :param num:
        :param my_string:
        """
        instance = super().__new__(cls)
        cls.numbers.append(number)
        cls.values.append(value)
        return instance


    def __init__(self, number: int, value: str):
        self.number = number
        self.value = value


    def __str__(self):
        return f'Archive({self.number}, {self.value})'

    def __repr__(self):
        return f'Archive({self.number}, {self.value})'

a_1 = Archive(1, 'Один')
a_2 = Archive(2, 'Два')
print(a_1.numbers, a_1.values)
print(a_2.numbers, a_2.values)
print(a_1)
print(a_2.__repr__())