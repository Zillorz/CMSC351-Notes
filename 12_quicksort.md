# Quicksort

PRACTICE: Leetcode 912 (won't work, as leetcode 912 requires pattern hardness)

```py
def quick_sort(nums: list[int]):
    def partition(nums: list[int], start: int, end: int):
        pivot = end # great pivot selection (use median of 3 or random for a better choice)!
        t = start

        for i in range(start, end):
            if nums[i] <= nums[pivot]:
                swap(nums, t, i)
                t += 1

        swap(nums, t, end)
        return t


    def quick_sort_aux(nums: list[int], start: int, end: int):
        if start >= end: return

        pivot = partition(nums, start, end) 

        # sort our halves now
        quick_sort_aux(nums, start, pivot-1)
        quick_sort_aux(nums, pivot+1, end)

    quick_sort_aux(nums, 0, len(nums) - 1)
    return nums
```

Intro: Quicksort is a fast sorting alg for data which is fairly random.

In the real world there are better algs: Timsort, pdqsort (variant of quicksort), and splaysort
These do better with various datasets, including ones with sorted/kinda sorted sections

The Idea)
1. Pick some key that we will call the pivot
2. Partition the list such that all values less eq than M\[pivot\] are before, and all values greater are after (put equals anywhere)
3. Recursively sort the two halves (not including the pivot)

### Partitioning
swap p and the last element

Choose leftmost elt > pk
choose leftmost subsequent elt <= pk
swap those
repeat until not possible

Notice that partitioning is θ(n)

Choice of pivot: 
The best possible pivot is the median, but finding the median is HARD, and θ(n) with a large constant.
Other good ways are:
- Median of 3 (median of start, middle, and end)
- Random pivot (typical in the real world)

### The actual sort
Given some: `partition(array, start, end) -> index`

Then quicksort is simple
```jspeudo
function quicksort(A, L, R)
    if L < R:
        rpi = partition(A, L, R)
        quicksort(A, L, rpi - 1)
        quicksort(A, rpi + 1, R)
    end if
end function
```

### Details
A) Time:
- BC: if pk ends up in the middle (median) each time, 
      then we get the RR `T(n) = 2T(n / 2) + θ(n)` -> θ(nlgn)

- WC: if pk ends up at one end each time (min/max),
      then we get the RR `T(n) = T(n - 1) + θ(n)` -> θ(n^2)

- AC: if the pk ends up at a random place (our interpretation of avg) each time,
      in this case, T(n) = θ(nlgn)

B) Aux space:
- BC, we get the RR `S(n) = S(n / 2) + θ(1)` -> θ(lgn)
- WC, we get the RR `S(n) = S(n - 1) + θ(1)` -> θ(n)
- AC: in this case, S(n) = θ(lgn)

C) In place: Yes.
D) Stable: No, partitioning isn't stable.

## Limitations of Comparison-Based Sorting Algs

### Worst case

All of these sorting algorithms are, worst case: Ω(nlgn)

Practical Upshot?: 
No matter which sorting algorithm we use, 
for every n, there exists a list of length n which takes Ω(nlgn) time

### Decision tree

All of our CBSA work by comparing elements and reacting in response.
This means that CBSA can be represented as a *decision tree*.

Here is the D.T. for bubble sort with n=2

```
        [A, B]
      /       \
A>B  /         \ B <= A
    /           \
 [B, A]         [A, B]
```

More generally: we have a binary tree, where the root is the starting list, 
each branch is an act on the list, and the node is the result of that action.
This continues until the result of an action is the sorted list. 

Because the tree must handle all arrangements of a list, 
each leaf must be an permutation of the list, so the D.T. will have n! leaves.

We can then say that that the height of the tree h satisfies
$$
2^h \ge n!
h \ge \lg(n!)
h = \Omega(\lg(n!))
\text{Fun fact (not obvious at all): }\Omega(\lg(n!)) = \Omega(n\lg(n))
\text{So: } h = \Omega(n\lg n)
$$

Since each branch is a decision/action, and h is the height, at least h actions must be taken for some input list.
Which means, there is at least one list such that Ω(nlgn) actions must be made.

### Result
No matter which CBSA we use, (even new ones), there will always be a list which takes Ω(nlgn) time.

This also means, for any list which is only sortable through comparisons (infinite domains), our worst is case is at best Ω(nlgn).

However, non-comparison sorts can beat this! See radix and counting sort. These obviously won't work on infinite domain types (strings, etc..)
