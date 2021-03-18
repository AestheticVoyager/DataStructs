# DomirScire
# Stock Problem With Array DataStructure

A = [10,20,10,100, 101, 120]
# BruteForce Approach
# Time Complexity: O(n^2)
# Space Complexity: O(1)
def brute_force(A):
    max_profit=0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            max_profit = A[j] - A[i]
    return max_profit

# Smarter Approach
# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_sell(A):
    max_profit = 0.0
    min_price = A[0]
    for price in A:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit
