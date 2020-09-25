""" binary search algorithm """

def binary_search(array, value):
    low = 0
    high = len(array) - 1
    while low <= high:
        mid = (low + high)//2
        if array[mid] == value:
            return mid
        elif array[mid] < value:
            low = mid + 1
        else:
            high = mid - 1
    return -1
   
#start 
array = [1,2,3,4,5,6]
search_value = 7
result = binary_search(array, search_value)
print(f"The result is: {result}")