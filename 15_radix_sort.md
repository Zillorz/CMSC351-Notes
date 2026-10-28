# Radix Sort

PRACTICE: Leetcode 912 (no idea if this one works)

```py
def radix_sort(nums: list[int]):
    # normally our max-digit count would be passed to us
    d = int(log10(max(nums)) + 1)

    for i in range(d):
        # run our sorting algorithm on the digit D of our list
        counting_sort_on_digit(nums, i) # see sorts.py

    return nums
```

Requirements
- all items must have the same # of digits / chars, if not, left pad them
- those digits must be sortable have relative/order
- choose a underlying stable sorting alg, usually counting sort

Idea:
- Sort the list by the rightmost digit
- Then sort by the next rightmost

### Details

#### Time complexity w/counting sort
- If we use counting sort, we sort d times (where d is the number of digits)
- There are only k unique digits, so cs takes θ(n + k)
- This means radix sort takes θ(d(n + k))

Notes:
- typically k is constant. in base 10, there are only 10 different digits.  In the alphabet, there are only 26 letters, etc..
- This would give us complexity θ(dn)
- Often, d is also constant (think id numbers), then we get θ(n + k)
- If both are constant, it's θ(n) (nice)

Ex) If we're sorting UMD UID's then it's θ(n)
Ex) If we're sorting n binary numbers in range 0 to 2^n - 1, it takes θ(n^2)

#### Other

Stable: Yes
In place: Iff the underlying sort is, counting is not!
Aux space: Same as underlying sort, θ(n + k) for counting 
