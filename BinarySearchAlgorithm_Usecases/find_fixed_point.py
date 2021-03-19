"""
A fixed point in an array "A" is an index "i" such that A[i] is equal to "i".

Given an array of "n" distinct integers sorted in ascending order, write a function that returns a "fixed point" in the array.
If there is not a fixed point, return None
"""

# Time Complexity: O(n)
# Space Complexity: O(1)
def find_fixed_point_linear(A):
    for i in range(len(A)):
        if A[i] == i:
            return A[i]
    return None

# Because the array is sorted and distinct, we try binary search algorithm
# Time Complexity: O(log n)
# Space Complexity: O(1)
def find_fixed_point(A):
    low=0
    high=len(A)-1

    while low <= high:
        mid = (low+high) // 2

        if A[mid] < mid:
            low = mid+1
        elif A[mid] > mid:
            high = mid-1
        else:
            return A[mid]
    return None

if __name__ == "__main__":
    # fixed point is 3:
    # value 3 is at index 3
    A = [-10, -5, 0, 3, 7]
    print(find_fixed_point(A))

    # fixed point is 0:
    # value 0 is at index 0
    B = [0, 2, 3, 7]
    print(find_fixed_point(B))

    # no value is at the right index => None
    C = [-10, -5, 0, 1, 7]
    print(find_fixed_point(C))

