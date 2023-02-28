""" В модуле реализованы алгоритмы простого и бинарного поиска, а также сортировка слиянием."""

def simple_search(arr, key):
    """ Простой поиск"""
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1


def binary_search(arr, start, end, key):
    """ Бинарный поиск"""
    if start > end:
        return -1

    middle = start + (end - start) // 2

    if arr[middle] == key:
        return middle
    if arr[middle] > key:
        return binary_search(arr, start, middle - 1, key)

    return binary_search(arr, middle + 1, end, key)


def merge(arr, low, mid, high):
    """ Функция для записи отсортированного подмассива в оригинальный массив"""
    buffer = [None] * (high + 1 - low)
    h, i, j = low, 0, mid + 1

    while h <= mid and j <= high:
        if arr[h] <= arr[j]:
            buffer[i] = arr[h]
            h += 1
        else:
            buffer[i] = arr[j]
            j += 1
        i += 1

    if h > mid:
        for k in range(j, high + 1):
            buffer[i] = arr[k]
            i += 1
    else:
        for k in range(h, mid + 1):
            buffer[i] = arr[k]
            i += 1

    for k in range(0, high - low + 1):
        arr[low + k] = buffer[k]


def merge_sort(arr, low, high):
    """ Сортирует массив сортировкой слиянием"""
    if low < high:
        mid = (low + high) // 2
        merge_sort(arr, low, mid)
        merge_sort(arr, mid + 1, high)
        merge(arr, low, mid, high)
