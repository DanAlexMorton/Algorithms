import random

def partition(arr, low, high):
    i = ( low-1 )
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] < pivot:
            i = i+1
            arr[i],arr[j] = arr[j],arr[i] #swap the numbers in the array

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return ( i+1 )

def partitionRandom(arr, low, high):
    randomPivot = random.randrange(low, high) 

    arr[low],arr[randomPivot] = \
         arr[randomPivot],arr[low]  
    return partition(arr, low, high)

def quickSort(arr, low, high):

    if low < high:
        #to use the random quickSort replace partition with partitionRandom
        pivotIndex = partitionRandom(arr,low,high)

        quickSort(arr, low, pivotIndex-1)
        quickSort(arr, pivotIndex+1, high)

  #Below is code to test the quick sort algorithm 
  #Partion-QuickSort algorithm use partition(arr,0,n-1) instead of quickSort(arr,0,n-1)     

arr = [8, 7, 1, 9, 11, 5, 6]
n = len(arr)
partition(arr,0,n-1)
print("Sorted Array is: ")
for i in range(n):
    print("%d" %arr[i]),

