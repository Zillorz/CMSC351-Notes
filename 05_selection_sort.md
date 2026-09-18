# Selection Sort

PRACTICE: Leetcode 912 (selection sort will be too slow, so time limit exceeded is expected)

```py
def selection(nums: list[int]):
    n = len(nums)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        if i != min_idx:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums
```

The Idea)
1. Find the smallest element A_i. 
2. Swap A_0 and A_i
3. Repeat with A\[1..]

Ex)
```
A = [2 5 2' 3 1 4] # Note, 2' is the same as 2, just marked for stability

1) [1 5 2' 3 2 4]
2) [1 2' 5 3 2 4]
3) [1 2' 2 3 5 4]
4) [1 2' 2 3 5 4] # this step does nothing as the smallest element is 3
5) [1 2' 2 3 4 5]
```

### Details
The time complexity is: $\theta(n^2)$
- conditional takes time $c_1$
- minindex=i and swap take time $c_2$
- so $T(n) = \sum_{i=0}^{n-2} (c_2 + \sum_{j=i+1}^{n-1} c_1)$
 
Stability: NO, see ex
In-Place: YES
Auxiliary Space: $\theta(1)$ or 4 (i, j, min_idx, swap varible - not in this case)
