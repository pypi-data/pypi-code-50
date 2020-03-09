def selectionSort(array):
    for i in range(len(array)):
        min_idx = i 
        for j in range(i+1, len(array)):
            if array[min_idx] > array[j]:
                min_idx = j 
        array[i], array[min_idx] = array[min_idx], array[i]
    return array

def bubbleSort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
    return array

def recursiveBubbleSort(array):
    for i, num in enumerate(array):
        try:
            if array[i+1] < num:
                array[i] = array[i+1] 
                array[i+1] = num 
                bubbleSort(array) 
        except IndexError:
            pass
    return array 

def insertionSort(array):
    for i in range(1, len(array)):
        key = array[i]
        j = i-1
        while j >= 0 and key < array[j]:
                array[j + 1] = array[j]
                j -= 1
        array[j + 1] = key
    return array

def mergeSort(array):
    if len(array) >1:
        mid = len(array)//2
        L = array[:mid]
        R = array[mid:]

        mergeSort(L)
        mergeSort(R) 

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                array[k] = L[i] 
                i+=1
            else:
                array[k] = R[j] 
                j+=1
            k+=1
        
        while i < len(L):
            array[k] = L[i] 
            i+=1
            k+=1
        
        while j < len(R):
            array[k] = R[j] 
            j+=1
            k+=1
    else:
        return array

    return array

def iterativeMergeSort(array):
    def merge(a, l, m, r):
        n1 = m - l + 1
        n2 = r - m 
        L = [0] * n1 
        R = [0] * n2 
        for i in range(0, n1):
            L[i] = a[l + i] 
        for i in range(0, n2):
            R[i] = a[m + i + 1] 
    
        i, j, k = 0, 0, l 
        while i < n1 and j < n2:
            if L[i] > R[j]:
                a[k] = R[j] 
                j += 1
            else:
                a[k] = L[i] 
                i += 1
            k += 1
    
        while i < n1:
            a[k] = L[i] 
            i += 1
            k += 1
    
        while j < n2:
            a[k] = R[j] 
            j += 1
            k += 1
    
    current_size = 1
    while current_size < len(array) - 1:
        left = 0
        while left < len(array)-1:
            mid = left + current_size - 1
            right = ((2 * current_size + left - 1, 
                    len(array) - 1)[2 * current_size  
                          + left - 1 > len(array)-1])
            merge(array, left, mid, right) 
            left = left + current_size*2
        current_size = 2 * current_size
    return array

def quickSort(array):
    def partition(array, low, high):
        i = ( low-1 )
        pivot = array[high]
        for j in range(low, high):
            if   array[j] <= pivot:
                i = i+1 
                array[i],array[j] = array[j],array[i] 
        array[i+1],array[high] = array[high],array[i+1] 
        return ( i+1 )
    def sort(array, low, high):
        if low < high:
            pi = partition(array,low,high)
            sort(array, low, pi-1) 
            sort(array, pi+1, high)

    sort(array, 0, len(array)-1)
    return array

def headSort(array):
    def heapify(array, n, i): 
        largest = i
        l = 2 * i + 1
        r = 2 * i + 2
        if l < n and array[i] < array[l]: 
            largest = l
        if r < n and array[largest] < array[r]: 
            largest = r
        if largest != i: 
            array[i],array[largest] = array[largest],array[i]
            heapify(array, n, largest)
    def heap(array): 
        n = len(array)
        for i in range(n, -1, -1):
            heapify(array, n, i)
        for i in range(n-1, 0, -1):
            array[i], array[0] = array[0], array[i]
            heapify(array, i, 0)
    heap(array)
    return array

def countingSort(array):
    """
    For strings
    """
    output = [0 for i in range(256)]
    count = [0 for i in range(256)]
    ans = ["" for _ in array]
    for i in array:
        count[ord(i)] += 1
    for i in range(256):
        count[i] += count[i-1]
    for i in range(len(array)):
        output[count[ord(array[i])]-1] = array[i] 
        count[ord(array[i])] -= 1
    for i in range(len(array)):
        ans[i] = output[i] 
    
    return ans

def radixSort(array):
    pass

def bucketSort(array):
    pass

def shellSort(array):
    pass

def timSort(array):
    pass

def combSort(array):
    pass

def pigeonHoleSort(array):
    pass

def cycleSort(array):
    pass

def cocktailSort(array):
    pass

def strandSort(array):
    pass

def bitonicSort(array):
    pass

def pancakeSort(array):
    pass

def binaryInsertionSort(array):
    pass

def bogoSort(array):
    pass

def permutationSort(array):
    return bogoSort(array)

def gnomeSort(array):
    pass

def sleepSort(array):
    pass

def tagSort(array):
    pass

def treeSort(array):
    pass

def cartesianTreeSort(array):
    pass

def jackSort(array):
    pass

if __name__ == "__main__":
    pass
    result = quickSort([4, 2, 5, 6])
    print(result)
