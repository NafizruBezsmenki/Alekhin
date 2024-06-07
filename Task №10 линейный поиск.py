def linear_search(list, target):
    for i in range(len(list)):
        if list[i] == target:
            return i
    return -1

if __name__ == "__main__":
    list = [10, 20, 30, 40, 50]
    target = 10
    result = linear_search(list, target)
    print('Исходный массив: ', list)

    if result != 1:
        print(f"Номер элемента {target}: {result + 1}")
    else:
        print('Элемент не найден')

