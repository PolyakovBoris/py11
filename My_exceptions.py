class My_exception(Exception):
    """Базовый класс мои исключения для использования в классе Matrix (создание матрицы)"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'{self.value}'

class Matrix_size_input_error(My_exception):
    """Ошибка ввода размера матрицы"""
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f'вы ввели "{self.value}", введите целое число '

class Matrix_size_difference(My_exception):
    """Ошибка разные размеры матриц при сложении"""
    def __init__(self,name1, name2):

        self.name1 = name1
        self.name2 = name2


    def __str__(self):
        return f'можно складывать только однопорядковые матрицы'


