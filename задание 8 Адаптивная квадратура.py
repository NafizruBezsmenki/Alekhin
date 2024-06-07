import math
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
def adaptive_integration(integration_func, func, a, b,tol):
    """
    Вычисляет интеграл функции методом адаптивной квадратуры.

    :param integration_func: Базовая функция интегрирования, например, trapezoid_integration или rectangle_integration
    :param func: Функция, которую нужно интегрировать
    :param a: Нижний предел интегрирования
    :param b: Верхний предел интегрирования
    :param tol: Точность, с которой необходимо вычислить интеграл
    :return: Приближенное значение интеграла
    """
    def integrate(a, b):
        prev_F = integration_func(func, a, b, n=1)
# Вычисляем интеграл на отрезке [a, b]
        F = integration_func(func, a, b, n=2)

# Вычисляем погрешность
        err = math.fabs(F - prev_F) / 15

        if err < tol:
            return F

# Разделяем отрезок пополам
        c = (a + b) / 2

# Рекурсивно вычисляем интегралы на двух половинках
        left = integrate(a, c)
        right = integrate(c, b)

        return left + right

# Выбираем начальное количество шагов
    n = 2

# Вычисляем интеграл
    prev_F = integrate(a, b)

    return prev_F
def func_example(x):
    return x**2-4*x+4

integral=adaptive_integration(rectangle_integration,func_example,0,2,0.00001)
print(f"Приближенное значение интеграла: {integral}")