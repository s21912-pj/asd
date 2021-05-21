import random

from SortAlgorithms import bubbleSort,mainQuickSort,heapSort


class AlgorithmPerformance:
    def invoke(self):
        randomlist = []
        for i in range(0, 180000):
            n = random.randint(1, 30)
        randomlist.append(n)
        sortedList = sorted(randomlist)
        reverseSorted = list(reversed(randomlist))
        randomBubbleSortTime = 0;
        randomQuickSortTime =0;
        randomHeapSortTime=0;

        sortedNumbersBubbleTime = 0;
        sortedQuickSortTime = 0;
        sortedHeapSortTime = 0;

        reversedSortedNumbersBubbleTime = 0;
        reversedSortedQuickSortTime = 0;
        reverseSortedHeapSortTime = 0;
        iteration = 1
        for i in range(iteration):

            randomBubbleSortTime += bubbleSort(randomlist)
            randomQuickSortTime += mainQuickSort(randomlist)
            randomHeapSortTime += heapSort(randomlist)

            sortedNumbersBubbleTime += bubbleSort(sortedList)
            sortedQuickSortTime += mainQuickSort(sortedList)
            sortedHeapSortTime += heapSort(sortedList)

            reversedSortedNumbersBubbleTime+=bubbleSort(reverseSorted)
            reversedSortedQuickSortTime+=mainQuickSort(reverseSorted)
            reverseSortedHeapSortTime+=heapSort(reverseSorted)

        print(str("BubbleSort with random numbers: ") + str("{0:.10f}".format(randomBubbleSortTime / iteration)))
        print(str("QuickSort with random numbers: ") + str("{0:.10f}".format(randomQuickSortTime / iteration)))
        print(str("HeapSort with random numbers: ") + str("{0:.10f}".format(randomHeapSortTime / iteration)))

        print(str("BubbleSort with sorted numbers: ") + str("{0:.10f}".format(sortedNumbersBubbleTime / iteration)))
        print(str("QuickSort with sorted numbers: ") + str("{0:.10f}".format(sortedQuickSortTime / iteration)))
        print(str("HeapSort with sorted numbers: ") + str("{0:.10f}".format(sortedHeapSortTime / iteration)))

        print(str("BubbleSort with reverse sorted numbers: ") + str("{0:.10f}".format(reversedSortedNumbersBubbleTime / iteration)))
        print(str("QuickSort with reverse sorted numbers: ") + str("{0:.10f}".format(reversedSortedQuickSortTime / iteration)))
        print(str("HeapSort with reverse sorted numbers: ") + str("{0:.10f}".format(reverseSortedHeapSortTime / iteration)))

if __name__ == '__main__':
    xx = AlgorithmPerformance()
    xx.invoke()
