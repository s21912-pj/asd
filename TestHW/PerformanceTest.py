import random


from HeapSortAlgo import heapSort as heapSortHW
from HeapSortAlgoInternet import heapSort as heapSortExt
from BubbleSortAlgo import bubbleSort
from QuickSortAlgo import qSort

class PerformanceTest:

    def count(self):
        randomlist = []
        for i in range(0, 500):
            n = random.randint(1, 50)
            randomlist.append(n)
        randomDict = {
            'randomNums': randomlist,
            'sortedNums': sorted(randomlist),
            'reverseSortNums': list(reversed(randomlist))
        }
        dictionary = { 'bubbleSortTime':0,
                       'heapSortHWTime':0,
                       'heapSortExtTime': 0,
                       'quickSortTime':0,
                       'sortedBubbleSortTime':0,
                       'sortedHeapSortTime':0,
                       'sortedHeapSortExtTime': 0,
                       'sortedQuickSortTime':0,
                       'reverseSortedBubbleSortTime':0,
                       'reverseSortedHeapSortTime':0,
                       'reverseHeapSortExtTime': 0,
                       'reverseSortedQickSortTime':0
                       }
        for i in range(100):
            for key,value in dictionary.items():
                dictionary[key]+=self.chooseAlgo(key,randomDict)
        sortedDict = sorted(dictionary.items(), key=lambda x: x[1])
        for key,value in sortedDict:
            print(str(key) + str(": {0:.10f}".format(dictionary[key] / 100)))


    def chooseAlgo(self,key, randomDict):
        if key=='bubbleSortTime':
            return bubbleSort(randomDict['randomNums'])
        if key == 'heapSortHWTime':
            return heapSortHW(randomDict['randomNums'])
        if key == 'heapSortExtTime':
            return heapSortExt(randomDict['randomNums'])
        if key == 'quickSortTime':
            return qSort(randomDict['randomNums'])
        if key == 'sortedBubbleSortTime':
            return bubbleSort(randomDict['sortedNums'])
        if key == 'sortedHeapSortTime':
            return heapSortHW(randomDict['sortedNums'])
        if key == 'sortedHeapSortExtTime':
            return heapSortExt(randomDict['sortedNums'])
        if key == 'sortedQuickSortTime':
            return qSort(randomDict['sortedNums'])
        if key == 'reverseSortedBubbleSortTime':
            return bubbleSort(randomDict['reverseSortNums'])
        if key == 'reverseSortedHeapSortTime':
            return heapSortHW(randomDict['reverseSortNums'])
        if key == 'reverseHeapSortExtTime':
            return heapSortExt(randomDict['reverseSortNums'])
        if key == 'reverseSortedQickSortTime':
            return qSort(randomDict['reverseSortNums'])


if __name__ == '__main__':
    obj = PerformanceTest();
    obj.count()