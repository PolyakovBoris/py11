import My_exceptions
from My_exceptions import Matrix_size_input_error
from My_exceptions import Matrix_size_difference
class Matrix:
    """
    Создаётся автозаполняемая матрица размером x,y
    """

    def __init__(self, name = 'unknown matrix'):
        self.name = name
        self.x = self.get_num_from_user_input()
        self.y = self.get_num_from_user_input()
        self.matrix = [[i + j for i in range(self.x)] for j in range(self.y)]

    def get_num_from_user_input(self):

        while True:
            num = input(f'введите размер матрицы {self.name} - ')

            try:
                if not str.isdigit(num):
                    raise Matrix_size_input_error(num)
                break
            except Matrix_size_input_error as e:
                print(e)

        return int(num)


    def __str__(self):
        """вывод в консоль матрицы"""
        return 'выводим матрицу\n' + '\n'.join('\t'.join(map(str, row)) for row in self.matrix)


    def __repr__(self):
        return f'объект матрица {self.name}\n' + '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

    def __add__(self, other):
        """
        сложение матриц
        """

        try:
            if (len(self.matrix) != len(other.matrix)) | (len(self.matrix[0]) != len(other.matrix[0])):
                raise Matrix_size_difference(self.name, other.name)
        except Matrix_size_difference as e:
            print(e)
            return

        new_matrix = Matrix()
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                new_matrix.matrix[i][j] = self.matrix[i][j] + other.matrix[i][j]
        return new_matrix

    def __eq__(self, other):
        """Сравнение матриц"""
        print(f'сравнивается матрица \n {self.name} \nи матрица \n {other.name}')
        return self.matrix == other.matrix


matr1 = Matrix('1')
matr2 = Matrix('2')

print(matr1 + matr2)
print(matr1 == matr2)
