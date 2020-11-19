import random

def partition(arr, fromIndex, toIndex):
    i = ( fromIndex -1 )
    pivot = arr[toIndex]

    for j in range(fromIndex, toIndex):
        if arr[j] < pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i] #swap the numbers in the array

    arr[i + 1],arr[toIndex] = arr[toIndex],arr[i + 1]
    return ( i + 1 )

def partitionRandom(arr, fromIndex, toIndex):
    randomPivot = random.randrange(fromIndex, toIndex) 

    arr[fromIndex],arr[randomPivot] = \
         arr[randomPivot],arr[fromIndex]  
    return partition(arr, fromIndex, toIndex)

def quickSort(arr, fromIndex, toIndex):

    if fromIndex < toIndex:
        #to use the random quickSort replace partition with partitionRandom
        pivotIndex = partitionRandom(arr,fromIndex,toIndex)

        quickSort(arr, fromIndex, pivotIndex -1)
        quickSort(arr, pivotIndex + 1, toIndex)

  #Below is code to test the quick sort algorithm 
  #Partion-QuickSort algorithm use partition(arr,0,n-1) instead of quickSort(arr,0,n-1)     

arr = [8, 7, 1, 9, 11, 5, 6]
n = len(arr)
partition(arr,0,n-1)
print("Sorted Array is: ")
for i in range(n):
    print("%d" %arr[i]),

