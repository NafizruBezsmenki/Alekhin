from numpy.linalg import det

def determinant(matrix):
    """
    Вычисляет детерминант матрицы.

    Args:
    matrix (list of list of float): Матрица для вычисления детерминанта.

    Returns:
    float: Детерминант матрицы.
    """
    n = len(matrix)

    # Если матрица не квадратная, возвращаем 0
    if n != len(matrix[0]):
        return 0

    # Если матрица 1x1, возвращаем единственный элемент
    if n == 1:
        return matrix[0][0]
    # Инициализируем детерминант нулем
    det = 0

    # Вычисляем детерминант по первому столбцу
    for j in range(n):
        # Получаем минор M1,j
        minor = [row[:j] + row[j+1:] for row in matrix[1:]]

        # Вычисляем детерминант минора
        det_minor = determinant(minor)

        # Добавляем к детерминанту (-1)^(i+j) * M1,j * det(M1,j)
        det += (-1)**(j) * matrix[0][j] * det_minor
    return det
matrix=[[666,777,545],[939,450,978],[12,74,28]]
print(determinant(matrix), det(matrix))