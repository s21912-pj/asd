import timeit


def heapSort(arr):
    start = timeit.default_timer()
    n = len(arr)
    for i in range((n-1)//2, -1, -1):
        heapify(arr,n,i)
    for i in range(n-1,0,-1):
        swap(arr,0,i)
        n-=1
        heapify(arr,n,0)
    stop = timeit.default_timer()
    return stop - start
def heapify(arr, heapSize,parentIndex):
    maxIndex = parentIndex
    leftNode = parentIndex*2+1
    rightNode = parentIndex*2+2
    if leftNode < heapSize and arr[leftNode]>arr[maxIndex]:
        maxIndex = leftNode
    if rightNode < heapSize and arr[rightNode]>arr[maxIndex]:
        maxIndex = rightNode
    if maxIndex!= parentIndex:
        swap(arr,maxIndex,parentIndex)
        heapify(arr,heapSize,maxIndex)
def swap(arr, max, parent):
    if max!=parent:
        arr[parent], arr[max] = arr[max], arr[parent]
