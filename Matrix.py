class Matrix:
    """
    Создаётся автозаполняемая матрица размером x,y
    """

    _X = 4
    _Y = 4

    def __init__(self, x = _X, y = _Y):
        self.matrix = [[i + j for i in range(x)] for j in range(y)]


    def __str__(self):
        """вывод в консоль матрицы"""
        return 'выводим матрицу\n' + '\n'.join('\t'.join(map(str, row)) for row in self.matrix)


    def __repr__(self):
        return f'объект матрица\n' + '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        """
        сложение матриц
        :param other:
        :return:
        """
        new_matrix = Matrix()
        for i in range(len(matr1.matrix)):
            for j in range(len(matr1.matrix[i])):
                new_matrix.matrix[i][j] = matr1.matrix[i][j] + matr2.matrix[i][j]
        return new_matrix

    def __eq__(self, other):
        """Сравнение матриц"""
        print(f'сравнивается матрица \n {self.matrix} \nи матрица \n {other.matrix}')
        return f'результат {self.matrix == other.matrix}'


matr1 = Matrix()
matr2 = Matrix()
new_matrix = matr1 + matr2
# print(repr(new_matrix))
print(matr1 == new_matrix)
