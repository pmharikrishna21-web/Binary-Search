def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high)
        if arr[mid] == target:
            return mid 
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1  
numbers = [2, 4, 7, 10, 23, 45, 70]
target_value = 23
result = binary_search(numbers, target_value)
print("Element found at index:",result)
