def brute_mcs(nums: list[int]):
    n = len(nums)
    max = nums[0]

    for i in range(n):
        rolling = 0
        for j in range(i, n):
            rolling += nums[j]

            if rolling > max:
                max = rolling


    return max

def dac_mcs(nums: list[int]):
    n = len(nums)

    if n == 1:
        return nums[0]

    # first we solve the left and right problems
    left_sol = dac_mcs(nums[:int(n/2)])
    right_sol = dac_mcs(nums[int(n/2):])

    # but what if the solution is in the middle?
    # then we need to solve

    lc_sum = nums[0]
    rc_sum = nums[int(n/2)]

    rolling = 0
    for i in range(int(n/2), n):
        rolling += nums[i]

        if rolling > rc_sum: rc_sum = rolling

    rolling = 0
    for i in range(int(n/2) - 1, -1, -1):
        rolling += nums[i]

        if rolling > lc_sum: lc_sum = rolling

    return max(max(lc_sum + rc_sum, left_sol), right_sol)

def kadane_mcs(nums: list[int]):
    n = len(nums)

    max = nums[0]
    min = 0 # here we store min { S_0,I }, start at 0, as we can choose not to pick an S_0,I
    sum = 0

    for j in range(n):
        sum += nums[j] # this is S_0,J
        max_j = sum - min # this is the max contiguous sum ending at J


        if max_j > max:
            max = max_j

        if sum < min: # update the min (if needed) so we can solve J+1
            min = sum

    return max


# less optimized Kadane, takes up more space
def dp_mcs(nums: list[int]):
    n = len(nums)
    dp = [0 for _ in range(n + 1)]

    for i in range(n):
        dp[i + 1] = dp[i] + nums[i]

    max = nums[0]
    min = dp[0]

    for i in range(1, n + 1):
        if dp[i] - min >= max:
            max = dp[i] - min

        if dp[i] <= min:
            min = dp[i]

    return max
