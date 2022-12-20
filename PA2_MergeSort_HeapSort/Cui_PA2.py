# -*- coding: utf-8 -*-

# Divide-and-Conquer - Merge Sort 
# Recursion form: T(n) = aT(n/b) + f(n)
# Python program for Merge Sort
import math
import numpy as np

mergeDepth = 0
totalNonRecursiveCost = {0:0, 1:0, 2:0, 3:0} # Key = depth, Value = Cost
totalRecursiveCost = 0  # Use the variable to track total recursive cost
leftNodeCost = 0        # Use the variable to track left node cost
rightNodeCost = 0       # Use the variable to track right node cost

def mergeSort(array, depth = 0, recursiveCall = False, part = "whole"):
    local_arr = np.array(array)
    global mergeDepth
    global totalNonRecursiveCost
    global totalRecursiveCost
    global leftNodeCost
    global rightNodeCost
    
    # Initialize cost variable
    if(depth == 0):
        mergeDepth = 0
        totalNonRecursiveCost = {0:0, 1:0, 2:0, 3:0}
        totalRecursiveCost = 0
        leftNodeCost = 0
        rightNodeCost = 0
    
    # For calculating depth only, not efficient but works
    if(len(local_arr) % 4 == 0 and len(local_arr) <= 4):
        depth = 1
        mergeDepth = 1
        
    elif(len(local_arr) % 2 == 0 and len(local_arr) <= 2):
        depth = 2
        mergeDepth = 2
    
    
    mergeDepth = max(depth, mergeDepth)
    print("Current node's depth is :  ", mergeDepth)
    print("Array in current depth is \n", local_arr)
    
    # Track the total recursive cost
    if(recursiveCall == True):
        totalRecursiveCost += 1
    
    # Track the cost of left or right node on each recursive call
    if(part == "left"):
        leftNodeCost += 1
    elif(part == "right"):
        rightNodeCost += 1
        
    print("Left Cost:  ", leftNodeCost, "   Right Cost   ", rightNodeCost)
    
    
    if len(array) > 1:
        mid = math.floor(len(array) / 2)    # Find the mid point of the array
        left = array[:mid]                  # Divide the input into left half
        right = array[mid:]                 # Divide the input into right half
        
        mergeSort(left, depth + 1, True, "left")                     # Recursively sort the left elements
        mergeSort(right, depth + 1, True, "right")                    # Recursively sort the right elements
        
        print("local array is \n", local_arr)
        
        i = j = k = 0                       # Use the index to compare the element in array   
        nonRecursiveCost = 0

        while i < len(left) and j < len(right):       # Compare the element in every recursive call and merge
            if left[i] < right[j]:
                array[k] = left[i]
                i += 1
            else:
                array[k] = right[j]
                j += 1
            k += 1
            nonRecursiveCost += 1
            print("  array is <> :  ", array)

        while i < len(left):                              # Copy remaining elements to array
            array[k] = left[i]
            i += 1
            k += 1
            nonRecursiveCost += 1
            print("  array is < left :  ", array)


        while j < len(right):
            array[k] = right[j]
            j += 1
            k += 1
            nonRecursiveCost += 1
            print("  array is < right :  ", array)

         # For calculating cost only, not efficient but works
        costDepth = 0
        if(len(local_arr) % 4 == 0 and len(local_arr) <= 4):
            costDepth = 1
            
        elif(len(local_arr) % 2 == 0 and len(local_arr) <= 2):
            costDepth = 2
            
        print("Non recursive cost is " , nonRecursiveCost , "on depth ", costDepth)
    
        # Compute total non-recursive cost
        totalNonRecursiveCost[costDepth] = totalNonRecursiveCost[costDepth] + nonRecursiveCost
    

# Chip-and-Be-Conquered - Heap Sort 
# Recursion form: T(n) = aT(n-b) + f(n)
# Python program for Heap Sort
            
# Heapify subtree - Max Heap
heapRecursiveCost = 0
heapNonRecursiveCost = 0
heapDepth = 0
totalHeapSortRecursiveCost = {} # Key = iteration number, Value = Recursive Cost

def heapify(array, size, index, isRecursive = False, iterNum = 0):
    global heapRecursiveCost
    
    largest = index          # Initialize largest val as root
    left = 2 * index + 1     # left = 2 * index + 1
    right = 2 * index + 2    # right = 2 * index + 2
 
    # Output left and right heap
    if(isRecursive):
        outputIdx = array[index]
        
        print("Iter num\n ", iterNum)

        # Calculate the heap cost
        heapRecursiveCost += 1
        print("Heap recursive cost\n ", heapRecursiveCost)
        
        print(" Index Value: ",outputIdx)
        if(left < size):
            print("  left child: ", array[left])
        
        if(right < size):
            print("  right child: ", array[right])

        print("Output array after heapify \n", array)
        totalHeapSortRecursiveCost[iterNum] = heapRecursiveCost

    
    # Check if the left child exists and is greater than root
    if left < size and array[largest] < array[left]:
        largest = left
 
    # Check if the right child exists and is greater than root
    if right < size and array[largest] < array[right]:
        largest = right
 
    # Replace root
    if largest != index:
        array[index], array[largest] = array[largest], array[index]
        
        # Heapify the root
        if(isRecursive == False):
            heapify(array, size, largest, isRecursive)   # Don't count the cost on this recursive Call
        else:
            heapify(array, size, largest, True, iterNum)   # Count the cost on this recursive Call
 
# Heap Sort
def heapSort(array):
    global heapNonRecursiveCost
    global heapDepth
    global heapRecursiveCost
    
    print("\nInput array for Heap sort is \n")
    size = len(array)
 
    # Build Max Heap
    for i in range(size // 2 - 1, -1, -1):
        heapify(array, size, i)                 # We don't build recursion tree during this step
        
    # Heap buil after the build
    print("!!!!! Array after max-heap build !!!!! \n", array)

    # Extract the element
    iterCount = 0
    for j in range(size - 1, 0, -1):            # Calculate recursive cost from here
        array[j], array[0] = arr[0], arr[j]     # Swap
        heapRecursiveCost = 0                   
        heapify(array, j, 0, True, iterCount)
        iterCount += 1
        
        # Calculate non-recursive cost
        heapNonRecursiveCost += 1
    
 

# Calls to calculate cost
def calculateLCM(array):
    print(np.lcm.reduce(array))

# Calls to print output
def printArray(array):
    npArray = np.array(array)
    print(npArray)
 
if __name__ == '__main__':
    
    # Merge Sort
    print("\n====================== Merge Sort Start =======================\n")
    arr = [13, 12, 10, 11, 15, 14, 16, 17]
    mergeSort(arr, 0, False)
    print("\nSorted array after merge sort is \n")
    printArray(arr)
    print("Total Non-Recursive Cost " , totalNonRecursiveCost)
    print("Total Recursive Cost " , totalRecursiveCost)
    print("====================== Divider =======================")

    # Uncoment the following code to test different case
    '''
    print("====================== Divider =======================")
    
    arr = [10, 11, 12, 13, 14, 15, 16, 17]
    mergeSort(arr, 0, False)
    print("\nSorted array after merge sort is \n")
    printArray(arr)
    print("Total Non-Recursive Cost " , totalNonRecursiveCost)
    print("Total Recursive Cost " , totalRecursiveCost)


    print("====================== Divider =======================")
    arr = [17, 16, 15, 14, 13, 12, 11, 10]
    mergeSort(arr, 0, False)
    print("\nSorted array after merge sort is \n")
    printArray(arr)
    print("Total Non-Recursive Cost " , totalNonRecursiveCost)
    print("Total Recursive Cost " , totalRecursiveCost)


    print("====================== Divider =======================")
    print("\n====================== Merge Sort End =======================\n")

    # Merge Sort End
    
    
    
    
    # Heap Sort Start
    print("\n====================== Heap Sort Start =======================\n")

    arr = [13, 12, 10, 11, 15, 14, 16, 17, 19, 18, 20, 21, 23, 22, 24]

    heapSort(arr)
    print("\nSorted array after Heap sort is \n")
    printArray(arr)
    
    print("Non-recursive cost of the heap sort is \n ", heapNonRecursiveCost)
    print("Total Heap Recursive by iter num: ",totalHeapSortRecursiveCost)
    print("Total Heap Recursive Cost: ",sum(totalHeapSortRecursiveCost.values()))
    print("====================== Divider =======================")

    
    arr = [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
    
    heapRecursiveCost = 0
    heapNonRecursiveCost = 0
    heapDepth = 0
    totalHeapSortRecursiveCost = {} # Key = iteration number, Value = Recursive Cost

    heapSort(arr)
    print("\nSorted array after Heap sort is \n")
    printArray(arr)
    
    print("Non-recursive cost of the heap sort is \n ", heapNonRecursiveCost)
    print("Total Heap Recursive by iter num: ",totalHeapSortRecursiveCost)
    print("Total Heap Recursive Cost: ",sum(totalHeapSortRecursiveCost.values()))
    print("====================== Divider =======================") 
    '''
     # Heap Sort Start
    print("\n====================== Heap Sort Start =======================\n")
    
    arr = [24, 23, 22, 21, 20, 19, 18, 17, 16, 15, 14, 13, 12, 11, 10]
    heapRecursiveCost = 0
    heapNonRecursiveCost = 0
    heapDepth = 0
    totalHeapSortRecursiveCost = {} # Key = iteration number, Value = Recursive Cost

    heapSort(arr)
    print("\nSorted array after Heap sort is \n")
    printArray(arr)
    
    print("Non-recursive cost of the heap sort is \n ", heapNonRecursiveCost)
    print("Total Heap Recursive by iter num: ",totalHeapSortRecursiveCost)
    print("Total Heap Recursive Cost: ",sum(totalHeapSortRecursiveCost.values()))
    print("====================== Divider =======================")

    
    
    
    
    
    
    
    
    
    
    