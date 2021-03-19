"""
Write a function that takes a non-negative int and returns the largest int whose square is less that or equal to the int given.
Example:
    Input is 300
    Output should be 17, since 17^2 = 289 < 300.
    Note that 18^2 = 324 > 300, so the number 17 is the correct answer.
"""

def integer_square_root(k):
    low=0
    high=k

    while low<=high:
        mid=(low+high)//2
        mid_squared=mid*mid

        if mid_squared <= k:
            low = mid + 1
        else:
            high= mid - 1
    return low - 1

if __name__ == "__main__":
    k = 300
    print(integer_square_root(k))
