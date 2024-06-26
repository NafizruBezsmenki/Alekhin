def rectangle_integration(func, a, b, n):
    """
    Вычисляет интеграл функции методом прямоугольников.

    :param func: Функция, которую нужно интегрировать
    :param a: Нижний предел интегрирования
    :param b: Верхний предел интегрирования
    :param n: Количество прямоугольников (шагов интегрирования)
    :return: Приближенное значение интеграла
    """
    h = (b - a) / n # Ширина прямоугольника

    sum = 0
    for i in range(n):
        x = a + i * h
        sum += func(x) * h

    return sum

    