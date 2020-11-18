def insertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

arr = [31, 41, 59, 26, 41, 58]
insertionSort (arr)
for i in range(len(arr)):
    print ("% d" % arr[i])
