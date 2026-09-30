# Recurrence Relations

Goal: Build a new tool which we can use to analyze time complexity.

### Inspiration

Suppose T(n) = time for [bubble sort](/04_bubble_sort.md) for a list of length n,

Our definition of bubble sort can be written as
1. Iterate through once, swapping elements as we go, correctly positioning n-1
2. Do bubble sort on 0..n-2

We can then write
$T(n) = cn + T(n-1)$, where cn is the time step 1 takes, and T(n-1) is the time step 2 takes

<hr>

Suppose T(n) = time for [binary search](/08_binary_search.md) for a list of length n,

Our definition of binary sort is
1. Check the middle element
    2. If greater then needle, search the 0 to middle-1
    2. If less then needle, search middle+1 to end 

We can then say
$T(n) = c + T(\frac{n}{2})$ (kind of, the T(n/2) isn't always called (element found?))

<hr>

Suppose T(n) = Time for [MCS](/03_maximum_contiguous_sum.md) divide and conquer, then we can say

$T(n) = cn + 2T(\frac{n}{2})$

## Info

Defn) A *recurrence relation* for T(n) is an expression for T(n) in terms of T(<n) a perhaps other expressions involving n

ex) $T(n) = 3T(\frac{n}{2}) + 5n$
ex) $T(n) = 2T(\frac{n}{5}) + \lg(n) + 1$
ex) $T(n) = T(n - 2) + 3$
ex) $T(n) = T(\frac{n}{2}) + T(\frac{n}{4}) + n + 1$

Comments
- Common to have floors or ceils, ex: $T(n) = 2T(\lceil\frac{n}{2}\rceil))$
- Common to have many bases cases, ex: $T(1) = 3$

### Uses

- Finding specific values of T(n)
- Finding a closed form for T, into which we can plug in n and get a value (in constant time).
- Finding asymptotic time complexity

#### Specific Value
ex)

$$
T(n) = 2T(\lfloor\frac{n}{3}\rfloor) + n + 1, T(0) = 5 
\\
\text{then }T(1) = 2T(0) + 1 + 1 = 12 
\text{then }T(2) = 2T(0) + 2 + 1 = 13 
\text{then }T(3) = 2T(1) + 3 + 1 = 28 
$$

#### Finding a closed form - digging down
ex)
$$
T(n) = T(\frac{n}{2}), T(1) = 5 
\\
T(n) = T(\frac{n}{2}) + 3
T(n) = (T(\frac{n}{4}) + 3) + 3 = T(\frac{n}{4}) + 6 
T(n) = (T(\frac{n}{8}) + 3) + 6 = T(\frac{n}{8}) + 9 
\dots
\\
\text{We can then say} 
T(n) = T(\frac{2}{n^k}) + 3k 
\\
T(1) = 5 \text{when} \frac{n}{2^k} = 1 
k = \lg{n} 
\\
T(n) = T(1) + 3\lg(n)
T(n) = 5 + 3\lg(n)
$$

ex)
$$
T(n) = T(n-1) + n, T(0) = 3
\\
T(n) = T(n-1) + n
T(n) = T(n-2) + (n-1) + n
T(n) = T(n-2) + (n-1) + n
\dots
\\
\text{We can then say} 
T(n) = T(n-k) + (n - k + 1) +  \dots + n
\\
T(0) = 3 \text{when} n-k = 0
k = n
\\
T(n) = 3 + (n - n + 1) + \dots + n
T(n) = 3 + 1 + \dots + n
T(n) = 3 + \sum_{i=1}^{n} i
T(n) = 3 + \frac{n \times (n + 1)}{2}
$$

Note: Finding T(n) makes finding asymptotic time complexities easy


1. First example: $T(n) = \theta(\lg n)$
2. Second example: $T(n) = \theta(n^2)$

For certain recurrence relations, we can go from recurrence relations to θ(f(n))
(this will be covered later)
