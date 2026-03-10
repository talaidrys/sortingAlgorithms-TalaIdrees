numbers = [8, 3, 12, 5, 1, 9]

#  Bubble Sort
def bubble_sort(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


#  Selection Sort
def selection_sort(arr):
    n = len(arr)
    arr = arr.copy()
    for i in range(n):
        min_index = i
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


#  Insertion Sort
def insertion_sort(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key
    return arr


print("Bubble Sort:", bubble_sort(numbers))
print("Selection Sort:", selection_sort(numbers))
print("Insertion Sort:", insertion_sort(numbers))