import time
import sys


def bubble(array):
    compare = 0
    swap = 0
    start_time = time.time()
    for final in range(len(array), 0, -1):
        exchanging = False
        for current in range(0, final - 1):
            compare += 1
            if array[current] > array[current + 1]:
                swap += 1
                array[current + 1], array[current] = array[current], array[current + 1]
                exchanging = True

        if not exchanging:
            break
    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": swap, "time": elapsed_time}


def selection(array):
    compare = 0
    swap = 0
    start_time = time.time()
    for index in range(0, len(array)):
        min_index = index

        for right in range(index + 1, len(array)):
            compare += 1
            if array[right] < array[min_index]:
                min_index = right
        swap += 1
        array[index], array[min_index] = array[min_index], array[index]
    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": swap, "time": elapsed_time}


def insertion(array):
    compare = 0
    swap = 0
    start_time = time.time()
    for p in range(0, len(array)):
        current_element = array[p]

        while p > 0 and array[p - 1] > current_element:
            compare += 1
            array[p] = array[p - 1]
            swap += 1
            p -= 1

        array[p] = current_element
        swap += 1

    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": swap, "time": elapsed_time}


def merge_sort(array):
    start_time = time.time()
    compare = merge(array)
    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": 0, "time": elapsed_time}


def merge(arr):
    compare = 0

    if len(arr) > 1:
        mid = len(arr)//2  # Finding the mid of the array
        left = arr[:mid]  # Dividing the array elements
        right = arr[mid:]  # into 2 halves

        merge(left)  # Sorting the first half
        merge(right)  # Sorting the second half

        compare = i = j = k = 0

        # Copy data to temp arrays left[] and right[]
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                compare += 1
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

    return compare


def quick_sort(alist):
    start_time = time.time()
    swap, compare = quick_sort_helper(alist, 0, len(alist)-1)
    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": swap, "time": elapsed_time}


def quick_sort_helper(alist, first, last):
    swap = 0
    compare = 0
    if first < last:
        splitpoint, swap, compare = partition(alist, first, last)
        quick_sort_helper(alist, first, splitpoint-1)
        quick_sort_helper(alist, splitpoint+1, last)
    return swap, compare


def partition(alist, first, last):

    pivotvalue = alist[int((first+last)/2)]
    leftmark = first+1
    rightmark = last
    done = False
    compare = 0
    swap = 0
    
    while not done:
        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark = leftmark + 1
            compare += 1
        else:
            compare += 1
        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1
            compare += 1
        else:
            compare += 1
        if rightmark < leftmark:
            done = True
        else:
            swap += 1
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp
    
    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp
    swap += 1
    
    return rightmark, swap, compare


def count_sort(array):
    swap = 0
    compare = 0

    start_time = time.time()
    maxval = max(array)
    m = maxval + 1
    count = [0] * m  # init with zeros
    for a in array:
        count[a] += 1  # count occurences
    i = 0
    for a in range(m):  # emit
        for c in range(count[a]):  # - emit 'count[a]' copies of 'a'
            array[i] = a
            i += 1
    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": swap, "time": elapsed_time}


def bucket_sort(alist):
    swap = 0
    compare = 0
    start_time = time.time()
    largest = max(alist)
    length = len(alist)
    size = largest / length

    buckets = [[] for _ in range(length)]
    for i in range(length):
        j = int(alist[i] / size)
        compare += 1
        if j != length:
            buckets[j].append(alist[i])
        else:
            buckets[length - 1].append(alist[i])

    for i in range(length):
        merge_sort(buckets[i])

    result = []
    for i in range(length):
        result = result + buckets[i]

    elapsed_time = round((time.time() - start_time), 5)

    return {"comparisons": compare, "swap": swap, "time": elapsed_time}
