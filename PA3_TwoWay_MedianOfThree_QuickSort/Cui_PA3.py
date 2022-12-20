# -*- coding: utf-8 -*-
import random

# 2-Way Quick Sort Implementation
# Partition
partition_execution_num = 0
def partition(A, p, r):
    global partition_execution_num
    x = A[r]            # pivot
    i = (p - 1)         # index of smaller element
    for j in range(p, r):
        partition_execution_num += 1
        # If the current element is smaller than or equal to pivot
        if A[j] <= x:
            i = i + 1
            A[i], A[j] = A[j], A[i]
  
    A[i + 1], A[r] = A[r], A[i + 1]
    # Print the execution numbers
    return (i + 1)

# 2-way partition Quick sort
quick_sort_execution_num = 0
def quickSort(A, p, r):
    global quick_sort_execution_num
    quick_sort_execution_num += 1
    if len(A) == 1:
        return A
    if p < r:
        # partition
        q = partition(A, p, r)
        # recursive call
        quickSort(A, p, q - 1)
        quickSort(A, q + 1, r)


  
  
# Test Quick Sort - Average Case
quick_sort_execution_num = 0
partition_execution_num = 0
print("======2-way partition Quick Sort=====")
for i in range(1, 5):
    test_size = 10 ** i
    
    random_int_list = random.sample(range(1, 1000000000), test_size)
    n = len(random_int_list)
    #print("Not sorted array is: ")
    #print(random_int_list)
    quickSort(random_int_list, 0, n-1)
    #print("Sorted array is: ")
    #print(random_int_list)
    print("Average-Test size is ", test_size)
    print("Average-Number of partition execution is ", partition_execution_num)
    # Print the execution numbers
    print("Average-Number of sort execution is ", quick_sort_execution_num)

# Test Sorted array - Worst-Case
sequence_int_list = []
quick_sort_execution_num = 0
partition_execution_num = 0

for i in range(1, 4):
    test_size = 10 ** i
    for j in range(1, test_size + 1):
        sequence_int_list.append(j)
        
    sequence_int_list.reverse()
    
    n = len(sequence_int_list)
    #print("Not sorted array is: ")
    #print(sequence_int_list)
    quickSort(sequence_int_list, 0, n-1)
    #print("Sorted array is: ")
    #print(sequence_int_list)
    print("Worst-Test size ", test_size)
    print("Worst-Number of partition execution is ", partition_execution_num)
    # Print the execution numbers
    print("Worst-Number of sort execution is ", quick_sort_execution_num)





# Median of three Quick Sort Implementation

# Calculate the median of three pivots
median_execution_num = 0
def median_of_three(A, l, r):
    global median_execution_num
    median_execution_num += 1
    mid = (l + r - 1) // 2
    a = A[l]
    b = A[mid]
    c = A[r-1]
    if a <= b <= c:
        return b, mid
    if c <= b <= a:
        return b, mid
    if a <= c <= b:
        return c, r - 1
    if b <= c <= a:
        return c, r - 1
    return a, l

# Partition around the median
partition_median_execution_num = 0
def partition_median(A, l, r):
    global partition_median_execution_num
    partition_median_execution_num += 1
    pivot, pivot_idx = median_of_three(A, l, r)
    A[l], A[pivot_idx] = A[pivot_idx], A[l]
    i = l + 1
    for j in range(l + 1, r, 1):
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]  
            i += 1
    A[l], A[i-1] = A[i-1], A[l] 
    return i - 1

# Quick sort with Median
quicksort_median_execution_num = 0
def quicksort_median(A, l, r):
    global quicksort_median_execution_num
    quicksort_median_execution_num += 1
    if l < r: 
        p = partition_median(A, l, r)  
        quicksort_median(A, l, p)  
        quicksort_median(A, p + 1, r)
    return A


# Test Median Quick Sort
partition_median_execution_num = 0
quicksort_median_execution_num = 0
median_execution_num = 0
print("======Median of three partition Quick Sort=====")
for i in range(1, 5):
    test_size = 10 ** i
    
    random_int_list = random.sample(range(1, 1000000), test_size)
    n = len(random_int_list)
    #print("Not sorted array is: ")
    #print(random_int_list)
    quicksort_median(random_int_list, 0, n)
    #print("Sorted array is: ")
    #print(random_int_list)
    
    # Print the execution numbers
    print("Average-Test size is ", test_size)
    print("Average-Number of median execution is ", median_execution_num)
    print("Average-Number of partition execution is ", partition_median_execution_num)
    print("Average-Number of sort execution is ", quicksort_median_execution_num)
    

# Test Sorted array on median - Worst-Case
sequence_int_list = []
partition_median_execution_num = 0
quicksort_median_execution_num = 0
median_execution_num = 0

for i in range(1, 4):
    test_size = 10 ** i
    for j in range(1, test_size + 1):
        sequence_int_list.append(j)
        
    sequence_int_list.reverse()
    
    n = len(sequence_int_list)
    #print("Not sorted array is: ")
    #print(sequence_int_list)
    quicksort_median(sequence_int_list, 0, n)
    #print("Sorted array is: ")
    #print(sequence_int_list)
    print("Worst-Test size ", test_size)
    print("Worst-Number of median execution is ", median_execution_num)
    print("Worst-Number of partition execution is ", partition_median_execution_num)
    print("Worst-Number of sort execution is ", quicksort_median_execution_num)