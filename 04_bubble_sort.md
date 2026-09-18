# Bubble Sort

PRACTICE: Leetcode 912 (bubble sort will be too slow, so time limit exceeded is expected)

```python
def sort(nums: list[int]):
    n = len(nums)

    for i in range(n):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                nums[j + 1], nums[j] = nums[j], nums[j + 1]

    return nums
```

The idea)

1. We have an array with length N. i is the iteration number
2. We scan from J = 0 to N-1-i, swapping if A\[j\] > A\[j + 1\] 
3. This guarantees that the last element N is sorted, so we then sort A\[0..N-1\] in the next iteration (2)


Example)
```
A = [8 4 3 4 1]
     4 8 3 4 1
     4 3 8 4 1
     4 3 4 8 1
    [4 3 4 1 8]
     3 4 4 1 8 
     3 4 4 1 8
    [3 4 1 4 8]
     3 4 1 4 8
    [3 1 4 4 8]
    [1 3 4 4 8]
```

The time complexity is: $\theta(n^2)$
 
Stability: YES
    Meaning: Identical elements stay in relative order

In-Place: YES
    Meaning: The list is sorted "on top of itself". By swapping, not making a new list/ds

Auxiliary Space: $\theta(1)$ or 3
    Meaning: The auxiliary space is the memory/space used not including the list

### Inversions

Definition) For a list A, an *inversion* is is pair of indices (i,j) w/ i<j but A_i > A_j.

Just a pair of indices out of order.

A list with no inversions is a sorted list.
A list sorted in descending order has `n choose 2` = $\frac{n(n - 1)}{2}$

Ex) `A = [5 1 3 4 2]`

Inversions are (0, 1) (0, 2) (0, 3) (0, 4), (2, 4), (3, 4)

**Bubble sort**

The number of times bubble sort swaps on A = The number of inversions on A.

So `bubble(A)` swaps 6 times
