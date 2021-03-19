"""
Given an array of sorted integers. Find the closest value to the given number.
Example:
    Input: arr[] = {1,2,4,5,6,7,9}
    Target number = 11
    Output = 9
    9 is the closest to 11 in given array
"""

def find_closest_num(A, target):
    min_diff = float("inf")
    low = 0
    high = len(A) -1
    closest_num = None

    # Edge Case for empty list or only one element
    if len(A) == 0:
        return None
    if len(A) == 1:
        return A[0]

    while low <= high:
        mid = (low + high) // 2

        if mid + 1 < len(A):
            min_diff_right = abs(A[mid+1] - target)
        if mid > 0:
            min_diff_left = abs(A[mid-1] - target)

        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = A[mid-1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = A[mid+1]

        # Move the midpoint
        if A[mid] < target:
            low = mid + 1
        elif A[mid] > target:
            high = mid - 1
        # if the element is the target, then
        else:
            return A[mid]
    return closest_num

if __name__ == "__main__":

    A = [1,2,4,5,6,6,8,9]
    target=7
    print(find_closest_num(A, target))

