"""
Define a bitonic sequence as a sequence of integers such that:
    x_1 <= ... <= x_k >= ... >= x_n-1 for some k, 0 <= k < n.

for example:
    1,2,3,4,5,4,3,2,1
    is a bitonic sequence.
    Write a program to find the largest element in such a sequence.
    We assume that  such a peak element exists.
"""

def find_highest_number(A):
    low = 0
    high=len(A)-1

    # Bitonic sequence requires at least 3 elements
    if len(A) < 3:
        return None

    while low <= high:
        mid = (low+high) // 2

        mid_left = A[mid-1] if mid - 1 > 0 else float("-inf")
        mid_right = A[mid+1] if mid + 1 < len(A) else float("inf")

        if mid_left < A[mid] and mid_right > A[mid]:
            low=mid+1
        elif mid_left > A[mid] and mid_right < A[mid]:
            high=mid-1
        elif mid_left < A[mid] and mid_right < A[mid]:
            return A[mid]

if __name__ == "__main__":
    # Peak is 5
    A=[1,2,3,4,5,4,3,2,1]
    print(find_highest_number(A))

    # No Peak
    B=[1,2,3,4]
    print(find_highest_number(B))

    # Less than 3 elements
    C=[1,2]
    print(find_highest_number(C))

    # Technically not a Bitonic Sequence but works, 6
    D = [1,6,5,4,3,2,1]
    print(find_highest_number(D))
