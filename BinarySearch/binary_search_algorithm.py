# DomirScire

# Data is a sorted list
data = [1,2,4,5,7,8,9,12,34,42,45,46,49,69]

# Linear Search Implementation
# N Time
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False

# Iterative Binary Search
# Log N Time
def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low+high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False


# Recursive Binary Search
# Log N Time
def binary_search_recursive(data, target, low, high):
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid-1)
        else:
            return binary_search_recursive(data, target, mid+1, high)

if __name__ == "__main__":
    target=69
    print(binary_search_iterative(data, target))
    print(binary_search_recursive(data, target, 0, len(data)-1))
