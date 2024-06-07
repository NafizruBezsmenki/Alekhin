import random

def monte_carlo_integration(func, bottom, top, n):
    s = 0.0

    for _ in range(n):
        point = random.uniform(bottom, top)
        s += func(point)

    area = (top - bottom) * (s / n)

    return area

def func_example(x):
    return x**2 - 4*x + 4
print(monte_carlo_integration(func_example, 0, 2, 10000))


