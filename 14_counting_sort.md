# Counting Sort

PRACTICE: Leetcode 912 (won't work, OOM)

```py
def counting_sort(nums: list[int]):
    n = len(nums)

    size = max(nums) # O(N) time!
    pos = [0 for _ in range(size+1)]

    for num in nums:
        pos[num] += 1

    for i in range(1, size+1):
        pos[i] = pos[i] + pos[i - 1]

    new_list = [0 for _ in range(n)]
    
    for i in reversed(range(n)):
        value = nums[i]
        new_list[pos[value] - 1] = value
        pos[value] -= 1

    for i in range(n):
        nums[i] = new_list[i]

    return nums
```

Counting sort is a non-CBSA sorting algorithm, normally used for non-negative integers.
This sort is limited, cannot sort all types.

Formally: If a type T has a bijective mapping F to $\mathbb{N}$ 
such that $a \in T, b \in T if a > b \text{then} F(a) > F(b)$

## The Idea
```
See the list A = [4 0 2 1 2 0]

Construct a list where the indexes correspond 
to the number of times that index shows up in the original list.

pos = [2 1 2 0 1]

Now, construct the sorted list by first accumulating pos

cumulative pos = [2 3 5 5 6]

In this list, Pos[i] = j. The last appearance of i is j-1 (if i shows up)

Proceed as follows: Go through A in reverse order
for each elt A[i] we look at Pos[A[i]] to tell us where it should go in the sorted ersionf of A,
put it there and decrement Pos[A[i]] in case another A[i] comes along.

The pseudocode is much clearer
```

### Details

Time: We have loops for both n and k, so our complexity is θ(n + k)

Notice that 
- if the k is the same for all N (sorting grades or something) then it's: θ(n)
- if our list of length n has numbers 0 to n^2, complexity is θ(n^2).

Aux Space: Θ(n + k)

Notice:
- Same as above.
- if k is big (sorting dollars that billionaires have), POS is really really big

In place: NO!
Stable: Yes, this is why the last step is in reverse order
