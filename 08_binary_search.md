# Binary Search

Idea)
1. To find a element in a sorted list we use binary search 
2. Compare the middle element and the value
    3. If the value > middle element: search the upper half
    4. If the value = middle element: solved!
    5. If the value < muddle element: search the lower half

```py
def search(nums: list[int], value: int):
    n = len(nums)

    l = 0
    r = n - 1

    while r > l:
        m = (l + r) // 2

        if nums[m] > value:
            r = m - 1
        elif nums[m] < value:
            l = m + 1
        else:
            return m

    return l
```

### Time

A) Best Case: $\theta(1)$, if target is first element checked
B) Worst Case: 
- We don't find the element, so the while loop iterates the most. 
- Each iteration, our search spaces / list length approximately halves 
- After iteration one, n/2, after iteration two, n/4 etc...
- When the list is size 1 (L=R), we exit
- $\frac{N}{2^k} = 1$, is our solution
- $k = \lg(N)$
- $T(n) = 1 + \lg(N)$
- $\theta(n) = \lg(n)$

This is a little informal/sloppy, not rigorous

(WIP, wrong currently)
C) Average Case:
- Let's assign each element a number, the number of iterations it would take
- On the first step, we can match exactly one element, so 1/n chance for that
- On the second step, we can match two elements, so 2/n chance for that
- On the third step, we can match four elements, so 4/n chance for that

- $1(\frac{1}{n}) + 2(\frac{2}{n}) + 3(\frac{4}{n}) ... + n(\frac{2^{n-1}}{n}) $
- $\frac{1}{n} \times (1 \times 1 + 2 \times 2 + 3 \times 4 + 4 \times 8 ...)$
- $\frac{1}{n} \times \sum_{i=1}^{\lg(n)} (i * 2^{i-1})$
- This is kinda equal to $\frac{1}{n} \times n\lg(n)$

- This also works on not perfect trees, but for that we need to manually sum everything

- See, $N = 2^k - 1$
- $1(\frac{1}{n}) + 2(\frac{2}{n}) ... n(2^{n-1} / n)$

- Turns into $\theta(\lg(n))$, not obvious
