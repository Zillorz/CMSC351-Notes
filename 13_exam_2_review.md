# Exam Review

## Overall
- don't memorize pseudocode but be familiar with it (only of which we saw, e.g. no heapsort)
- trace it
- odd prints + counters
- eat + sleep


### Insertion Sort
- high-level understandng
- pseudocode comments above
- inversions - what they are relv to insertion sort
- Time, BC: θ(n)     WC, AC: θ(n^2)
- Stable: Yes
- Aux: θ(1)
- In-place: Yes
- After k iterations of the main loop, the first k+1 elements are relatively (to one another) sorted 

### Binary Search
- List must be sorted
- How many iterations to reach a specific elt?
- If k iterations passed, how many elements could we have checked?
- Bc: θ(1)      WC, AC: θ(lg n)

### Rec. Relns
- Defn + Ex: T(n) = 2T(n/3) + n, 2T(n - 1) + 1
- Master thm
- Digging down
- Trees
- Go from pseudocode to recurrence relation
- Recurrence relation to high-level descriptions of algs (and other way)

#### Digging Down
- Goal: get a closed formula from a recurrence relation (T(n) = ____)
- method: 
    - iterate until we see a pattern
    - find a general exp involving k
    - use base case to solve for k
    - plug into general exp
- Know log/exp rules (e.g. simplify 4^lgn)

#### Trees
- RR -> Tree for T(Some Value)
- Tree + template -> RR: fill in T(n) = _ T(n / _) + _
- what do the values in the tree mean

#### Master Theorem
- Know it
- When it applies and when it doesn't
- Easy examples
    - fit well, no issues
- Other examples
    - Need you to do some tricks, like
    - lg(n) is O(n^ε)
    - n^c is O(n^c+d) for all d >= 1
    - n^c is Ω(n^c-d) for all d >= 1
    - etc...

### Merge sort
- How does the list change as it runs?
- RR: T(n) = 2T(n / 2) + Θ(n)
- Time: θ(nlgn), all cases
- Aux space: S(n) = S(n / 2) + θ(n), S(n) = θ(n)
- Stable: yes
- In place: No, merging

### Heaps
- Binary tree, Complete binary tree, Max Heap
- nodes 1-indexed, levels 0-indexed
- all indexing facts which result from that ^
- maxheapify: when can you call, what does it do
- converttomaxheap: what does it do: calls maxheapify on all nodes with children in reverse order

### Heap Sort
- list (treat as CBT). Convert to max heap
- run swap, chop, maxheapify process
- Time: wc: θ(nlgn), bc: θ(n) (if all elements are the same)
- Aux space: θ(1)
- Stable: No
- In place: Yes (our list is the heap)

### Quicksort
- High level explanation of partition
- Know **our** partition algorithm/process
- quicksort runs partition then rec calls
- Time: BC, AC: θ(nlgn), WC: θ(n^2)
- Aux space: BC, AC: θ(lg n), WC: θ(n) 
- Stable: No (partitioning)
- In place: Yes
