# Coin Changing

PRACTICE: Leetcode 322 (also try 518).

## The coin changing problem:

You are given an array with length N which has the denominations of coins.
You are then given a number Q which you want to build with these denominations.

Find the minimum number of coins which are worth Q.

## Hints:

Notice that a greedy[^1] algorithm is **NOT** always the optimal solution

Take the denominations `[1, 10, 25]` and the amount 30. A greedy algorithm will calculate: 25 + 1 + 1 + 1 + 1 + 1, which is 6 coins But, the optimal solution is: 10 + 10 + 10, which is 3 coins.

Think of this like strong induction, if you had the smallest number of coins for `0...Q-1`, how would you find Q.

## Insights:

A greedy solution is wrong unless the coins satisfy particular properties. The US coin system does work with greedy, but these arbitrary systems do not.

For the solution when we have the answer for `0...Q-1` is as follows:

Let's say DP is an array such that `DP[i]` has the optimal way to make the value i with the given denominations. An D is an array with length N which has the denominations given. Let us also assume `Q > max { D }` all values possible to create with the denomination.

Then, the answer for Q is `1 + min { DP[i - D_1], DP[i - D_2], .... DP[i - D_N] }`.

## Solution:

```python
def calculate(value: int, denominations: list[int]):
    dp = [-1] * (value + 1) # make a list with indexes 0 to value
    dp[0] = 0 # 0 coins needed to make 0

    for v in range(value+1):
        # At this point, we are trying to make coins worth v
        # we have the solutions to 0...V-1
        for c in denominations:
            # Now we will check some complexities we assumed earlier 
            bounds = v - c >= 0
            can_make = bounds and dp[v - c] != -1
            # either minimum or first viable combination of coins
            minimum = can_make and (dp[v - c] + 1 < dp[v] or dp[v] == -1)

            if minimum:
                dp[v] = 1 + dp[v - c]

    return dp[value]
```

Doing a quick complexity analysis, this algorithm is O(nq)
N: Number of coins
Q: Amount we are trying to make


[^1]: Always making the optimal or "greediest" choice at a step
