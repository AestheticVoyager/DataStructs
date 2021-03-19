# DomirScire
"""
Write a function that takes an array of sorted integers and a key, and returns the index of the first occurence of that key from the array.

Example:
    idx   0    1   2   3    4    5    6    7    8    9
    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108

    should return 3
"""

def find(A, target):
    low = 0
    high=len(A)-1

    while low <= high:
        mid = (low+high) // 2

        if A[mid] < target:
            low=mid+1
        elif A[mid] > target:
            high=mid-1
        else:
            if mid-1<0:
                return mid
            if A[mid-1] != target:
                return mid
            high=mid-1
    return None

if __name__ == "__main__":

    A = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 108
    print(find(A, target))

    B = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
    target = 285
    print(find(B, target))

