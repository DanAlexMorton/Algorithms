def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[largest] < arr[left]:
        largest = left
    
    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        heapify(arr, n, largest)

def heapSort(arr):
    n = len(arr)
    #Building Max Heap
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
    #Min Heap (comment out if you want a max heap only!)
    for i in range(n-1, 0, -1):
        #arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

arr = [27, 17, 3, 16, 13, 10, 1, 5, 7, 12, 4, 8, 9, 0]
heapSort(arr)
n = len(arr)
print("Sorted Array is: ")
for i in range(n):
    print("%d" % arr[i]),