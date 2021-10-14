#Assumes array is sorted. Alo takes O(log(n))
 
def binary_search(array, value):
    low = 0
    high = len(array) - 1
 
    while low <= high:
        mid = int((low+high)/2)
        if array[mid] == value:
            return mid
        elif array[mid] > value:
            high = mid - 1
        else:
            low = mid + 1
    return None
 
 
 
 
 
test_list = [1,3,9,11,15,19,29]
test_val1 = 25
test_val2 = 15
print(binary_search(test_list, test_val1))
print(binary_search(test_list, test_val2))