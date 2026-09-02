def calculate(value: int, denominations: list[int]):
    dp = [-1] * (value + 1) # make a list with indexes 0 to value, all 0
    dp[0] = 0

    for v in range(value+1):
        for c in denominations:
            # we need to ensure 3 things at this point
            # first, the coin is not bigger than the value v
            # second, we have a way to make v-c from our coins
            # third, the way to make v-c is the minimum
            # this condition below does that
            allowed = v - c >= 0 and dp[v - c] != -1 and (dp[v] == -1 or dp[v - c] + 1 <= dp[v])

            if allowed:
                dp[v] = 1 + dp[v - c]

    return dp[value]

print(calculate(24848, [1, 4, 9]))
