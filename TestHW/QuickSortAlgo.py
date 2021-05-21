import timeit


def qSort( arr: list):
    start = timeit.default_timer()
    quicksort(arr, 0, len(arr) - 1)
    stop = timeit.default_timer()
    return stop-start


def partition(arr, p, r):
    pivot = arr[r]
    smaller = p
    for i in range(p, r):
        if arr[i] <= pivot:
            arr[smaller], arr[i] = arr[i], arr[smaller]
            smaller = smaller + 1

    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller


def quicksort(arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q - 1)
        quicksort(arr, q + 1, r)