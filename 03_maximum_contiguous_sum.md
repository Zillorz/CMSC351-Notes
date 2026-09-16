# Maximum Contiguous Sum (mcs)

PRACTICE: Leetcode 53

### Intro
1. Useful problem
2. Lot's of different ways to solve it

A contiguous sublist is a subset of some list in order and contiguously (no skipped elements between start and end).

The sum of this is a contiguous sum.

> [!NOTE]
> The empty sublist is not allowed, the answer for the list \[-1\], is -1, not 0


#### Approach 1. Brute force

This solution checks all contiguous sums manually. It is $O(n^2)$

```python
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
```

#### Approach 2. Divide and Conquer

This is complicated but the idea is

Solve the problem for the left side of the list.
Solve the problem for the right side of the list.

if there is no left/right side, the list is n=1, return the first value

But what if the solution is in the middle? 
We actually manually check this like in the brute force case.

return the largest of the three (left sol, right sol, middle brute force)

```python
def dac_mcs(nums: list[int]):
    n = len(nums)

    if n == 1:
        return nums[0]

    left_sol = dac_mcs(nums[:int(n/2)])
    right_sol = dac_mcs(nums[int(n/2):])

    # now we find the largest sum on the left and right to make sure the sum doesn't cross our boundary
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
```

#### Approach 3. Kadane's algorithm

This is a space saving operation on the obvious dynamic programming solution to this problem.

Detailed)
0. Define S_I,J as the sum from \[I, J\]
1. Notice the property S\_0,J - S_0,I = S_I,J when I < J
2. We know then that the maximum contiguous sum on \[0, J\] that ends at J is S\_0,J = S\_0,I for some 0 <= I < J, or just S\_0,J, as this covers ever contiguous sum ending at J
3. The biggest value for this contiguous sum is S\_0,J - min(S_0,I, 0)
4. Notice that if we solve S\_0,0 to S\_0,K in order, we can solve S\_0,K+1 if we have the minimum of S\_0,0 to S\_0,K

Simple)
(A) Define M_I be the maximum contiguous sum from \[0, I\]
(B) Obs: MCS ending at i is either A\[i\] or A\[i\] + MCS ending at i - 1


```python
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
```
