def BubbleSorting(arr):
    """Args:
    arr(list of int):"""
    for j in range(len(arr)):
        for i in range(len(arr)-1):
            if arr[i] > arr[i + 1]:
                tmp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = tmp
    return arr