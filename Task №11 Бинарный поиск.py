def binary_search(target, arr):
    """
    Производит бинарный поиск элемента в отсортированном списке.

    :param target: элемент, который нужно найти
    :param arr: отсортированный список элементов, в котором осуществляется поиск
    :return: индекс найденного элемента или -1, если элемент не найден
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1

