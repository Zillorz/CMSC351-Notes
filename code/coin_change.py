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
