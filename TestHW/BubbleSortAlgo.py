import timeit


def bubbleSort(arr):
    n = len(arr)
    start = timeit.default_timer()
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    stop = timeit.default_timer()
    return stop - start