def bubbleSort(array):
    n = len(array)
    if n <= 1:
        return
    flag = False
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
                flag = True
        if not flag:
            break


if __name__ == '__main__':
    bubs = [1, 2, 4, 2, 6, 3, 7, 2, 34]
    bubbleSort(bubs)
    print(bubs)
