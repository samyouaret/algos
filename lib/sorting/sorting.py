

def bubble_sort(arr):
    last_index = len(arr) - 1
    for i in range(last_index):
        for j in range(last_index-i-1):
            # optimize for already sorted array stop when no longer 
            # there is a Swap
            swapped = False
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            if not swapped:
                break
    return arr


def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        # Assume the current index has the smallest value
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j  # Update min_index if a smaller element is found

        # Swap the found minimum element with the first element
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr
