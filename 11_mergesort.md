# Mergesort 


PRACTICE: Leetcode 912

```python
def merge_sort(nums: list[int]):
    n = len(nums)

    if n <= 1: return nums

    def merge(first: list[int], second: list[int]):
        combined: list[int] = []

        fp = 0
        sp = 0

        while fp < len(first) or sp < len(second):
            if not (sp < len(second)) or (fp < len(first) and sp < len(second) and first[fp] < second[sp]):
                combined.append(first[fp])
                fp += 1
            else:
                combined.append(second[sp])
                sp += 1

        return combined


    left = merge_sort(nums[:n//2])
    right = merge_sort(nums[n//2:])
    return merge(left, right)
```

### merge()

Merge takes two sorted lists, a and b, and combines them into one sorted list.

Time complexity: θ(length of lists)
Space complexity: θ(length of lists)

The python code uses multiple lists to make the methods simpler, but in a better implementation,
merge takes a list and split index, and merges the list into a temp, and writes the temp to the input

### Merge Sort
Given a list A of length n:

Base: if the list is of length n, return, as it's solved

A) Divide the list in half, if odd, add the extra element to the left
B) Recursively call merge sort on each half
C) Merge the two halves

### Time/Space Complexity + Extras

A) Time: T(n) = 2T(n/2) + n
Using the master theorem, we get θ(nlgn)

B) Space: S(n) = n + c, θ(n)
See that we can reuse the list tmp that we copy with.
Also notice that the subcalls for merge_sort use the SAME memory, 
as they do not use memory at the same time, so we only count it once!

C) In-Place: No, we use a temp list to merge
D) Stable: Yes, when elements are equal, the left ones are copied first


