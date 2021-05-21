import timeit

#bubbleSort
def bubbleSort(arr):
    start = timeit.default_timer()
    n = len(arr)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    stop = timeit.default_timer()
    return stop - start


#QuickSort
def mainQuickSort(arr: list):
    start = timeit.default_timer()
    quicksort(arr, 0, len(arr) - 1)
    stop = timeit.default_timer()
    return stop - start

def partition(arr, p, r):
    pivot = arr[r]
    smaller = p
    for i in range(p, r):
        if arr[i] <= pivot:
            arr[smaller], arr[i] = arr[i], arr[smaller]
            smaller = smaller + 1

    arr[smaller], arr[r] = arr[r], arr[smaller]
    return smaller


def quicksort( arr, p, r):
    if p < r:
        q = partition(arr, p, r)
        quicksort(arr, p, q-1)
        quicksort(arr, q + 1, r)


def heapSort(arr):
    start = timeit.default_timer()
    n = len(arr)
    buildHeap(n, arr)
    for i in range(n - 1, 0, -1):
        swap(arr, 0, i)
        n -= 1
        heapify(arr, n, 0)

    stop = timeit.default_timer()
    return stop - start


def buildHeap(n, arr):
    for i in range((n - 1) // 2, -1, -1):
        heapify(arr, n, i)


def heapify(arr, heapSize, parentIndex):
    maxIndex = parentIndex;
    leftNode = parentIndex * 2 + 1;
    rightNode = parentIndex * 2 + 2;
    if leftNode < heapSize and arr[leftNode] > arr[maxIndex]:
        maxIndex = leftNode
    if rightNode < heapSize and arr[rightNode] > arr[maxIndex]:
        maxIndex = rightNode
    if maxIndex != parentIndex:
        swap(arr, maxIndex, parentIndex)
        heapify(arr, heapSize, maxIndex)


def swap(arr, max, parent):
    if max != parent:
        arr[parent], arr[max] = arr[max], arr[parent]

