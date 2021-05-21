def sortArr(array):
    n = len(array)
    for i in range(n - 1, -1, -1):
        max = 0
        for j in range(0, i + 1, 1):
            if array[j] > array[max]:
                max = j
        array[i], array[max] = array[max], array[i]

if __name__ == '__main__':
    array = [0, 1, 1, 0, 1, 0 ,1]
    sortArr(array)
    print(array)
