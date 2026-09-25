# Insertion Sort2

PRACTICE: Leetcode 912 (insertion sort will be too slow, so time limit exceeded is expected)

```python
def insertion(nums: list[int]):
    n = len(nums)

    for i in range(1, n):
        j = i

        while j > 0 and nums[j] < nums[j - 1]:
            swap(nums, j, j - 1)
            j -= 1

    return nums
```

The idea)
    1. We maintain a sorted list on the left of our list, starting with the first element
    2. We then slide (swap backwards) the next element until it is in order in our sorted list
    3. repeat until all elements are added to our sorted list

Sorted portion is underlined
```
iteration i = 0
5 3 1 2 6 4
-

iteration i = 1
3 5 1 2 6 4
---

iteration i = 2
1 3 5 2 6 4
-----
iteration i = 3
1 2 3 5 6 4
-------
iteration i = 4
1 2 3 5 6 4
---------
iteration i = 5
1 2 3 4 5 6
-----------
```

### Time Complexity

While loops are tricky, we don't know how many times they run.

- Let's say the for loop body, excluding the while takes time $c_1$
- Then w/out the while look, it takes $\text{time} = c_1(n - 1)$

- In our example, we swapped 7 times (5, 3, 1, 2, 6, 4)
- This list also has 7 inversions!
- In fact, it can be shown each swap fixes one inversion
- This means that over the entire list, the while loop runs the \#inversions times

- So, the total time complexity is $T(n) = c_1(n - 1) + c_2(\text{#inversions})$
- where c_2 is the time the while loop body takes

This dependence on inversions actually makes it so that our best and worse case are different speeds!

So,
Best Case: 
- 0 inversions, so $T(n) = c_1(n - 1)$
- $\theta(n)$

Worse Case:
- Max inversions, so $T(n) = c_1(n - 1) + c_2(\frac{n \times (n - 1)}{2})$
- $\theta(n^2)$

Average Case:
- Need to be careful
- Let's take an average to be the average inversions in all n! lists
- In this case, a list of N has on average $\frac{n \times (n - 1)}{4}$ lists
- $T(n) = c_1(n - 1) + c_2(\frac{n \times (n-1)}{4})$
- $\theta(n^2)$

Stable: Yes
Aux Space: $\theta(1)$, just i and j
In-place: Yes
