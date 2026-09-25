# Exam Review

## Info

### Logisitics (skip)
- Arrive at 8:55am
- Sit every other seat
- Hw 3 due 6pm night before (tues)
- Sleep and eat

### General comments
- HW 1-3 ([coin changing](/01_coin_changing.md) to [selection sort](/05_selection_sort.md))
- Priority: Sample exams > HW > Notes
- Pre-351 stuff, not covered

- Don't memorize the pseudocode, but understand the algorithms
- No code writing
- **Pseudocode mods**: Insert print statement, counters
- No difficult arithmetic, calculations are managable
- Know **weak induction**, often used (problem 3 on hw is good)
- Know **time complexities**

## Review

### Coin Changing
- min \#coins to get some total
- greedy (not optimal)
- Alg which codes give optimal (dp), know it + mods
- See hw 1 problem
- Be familiar w/ some C=\[...\], basic ones which are greedy-optimal and are not

### $O(n)\text{, }\Omega(n)\text{ and }\theta(n)$
- Know visually what's going on
- Know the formal definitions 
- **WILL BE A O(n) or $\Omega(n)$ question**, it will ask you to prove **from definition**
- Know limit thms.
- Know Intuition
- A problem will specifically tell you to use either the limit theorems or definitions
- Know basic definitions and L'hôpitals
- Know "nice" fns.
- Know "tricks":
    - T/F: Bubble sort is O(n^10)
    - T/F: Bubble sort is $\theta(n^{10}))$    
    - T/F: Sel. sort is $\Omega(1)$
    - Answers: T, F, T

#### Time
- Time is a exact function T(n)
- Ex) $T(n) = c_2 n^2 + c_1 n + 3$
- Time complexity is one of the functions above
- Ex) $T(n) = \theta(n^2)$
- If theta, omega, or O is not asked for explicitly, find T(n)

### MCS
- Know what we're finding
- Brute force (Not covered)
- Divide & Conquer
    - Do it on a small list with print statements
    - $T(n) = \theta(n * \lg{n})$
- Kadanes's Algorithm
    - Fill in blanks (hw)
    - $T(n) = \theta(n)$

### Sorts

#### Bubble sort
- High level function
    - Sweeps through swapping out of order
    - After i iterations of outer loop, last i elements are correctly positioned and sorted
- Trace pseudocode
- $T(n) = \theta(n^2)$
- Stable: Yes, (relative order of equal elements is preserved)
- In-place: Yes, (sorts "on top" of the list)
- Aux space: $\theta(1)$
- Print statements / counters
    - Can be in weird places, like **mid swap**

- **inversions**
    - defn/counting
    - The number of swaps in bubble sort = \# of inversions
    - Inversions are on **indices**

#### Selection sort
- High level function
    - Chooses smallest element
    - After i iterations of the outer loop, the first i elements are correct
- Trace pseudocode
- $T(n) = \theta(n^2)$
- Stable: No, (be able to show an example)
- In-place: yes
- Aux space: $\theta(1)$
- **mid-swap** prints + counters
