# Heaps

Practice: https://leetcode.com/problem-list/heap-priority-queue/ (so so many)
Also: Leetcode 912 (fun fact, this is the first sort fast enough to pass!)

#### Binary Trees

Defn: A binary tree is a tree in which each node has at most two children
Defn: A **complete** binary tree is a binary tree in which all levels are full except the last. In the lowest level, all the nodes are "on the left"

All binary trees have a list equivalent, and the reverse.
- We 1-index these

**Why 1-index?**
This makes it so the node with index i, has children 2i and 2i + 1
Conversely, the node with index j, has parent $\lfloor\frac{j}{2}\rfloor$

A completely binary tree with N nodes has $\lfloor\frac{N}{2}\rfloor$ nodes with chilren

**More**
- The leftmost node in level j has index 2^j
- The node w/ index i i son level $\lfloor\lg i\rfloor$
- If a CBT has n nodes, it has $\lfloor\lg n\rfloor$ levels (see above)

### Max Heaps
A *max heap* is a CBT in which the a node's key >= it's childrens keys


Converting: Given a CBT how can we convert it to a MH in place by swapping nodes.

There are two functions which we'll use to do this!

A) **maxheapify** (aka swap key down)
    - it compares itself to it's children, swapping (with the larger of the two) if a child is larger
    - It then repeats the first step until it is larger than both children

Key property: maxheapify will turn a node with two max heap subtrees into a max heap.
BC: $\theta(1)$, children are smaller than key
WC: $\theta(\lg n)$

B) **converttomaxheap**
    - Notice that all leafs (nodes with no children) are already technically max heaps
    - We call maxheapify on the lowest layer with kids, then go up a layer and continue
    - = Call maxheapify on $\lfloor\frac{n}{2}\rfloor \dots 0$
    - We're left with a max heap!

BC: $\theta(n)$, already a max heap, no swaps
WC:
maxheapify is worst case $O(\lg n)$, we call this function on all n nodes, so
$O(n\lg n)$

Note: more precise analysis can get us a worse case bound of $\theta(n)$!

## Heap Sort

```python
def heap_sort(nums: list[int]):
    n = len(nums)
    
    # lc -> left child
    # rc -> right child
    def lc(i: int): return 2 * i + 1
    def rc(i: int): return 2 * i + 2

    # this function takes a element with two max heaps as children, and converts it to a max heap
    def max_heapify(nums: list[int], idx: int, len: int):
        if idx >= len: return

        if rc(idx) < len and nums[rc(idx)] > nums[idx] and nums[rc(idx)] >= nums[lc(idx)]:
            swap(nums, rc(idx), idx)
            max_heapify(nums, rc(idx), len)
        elif lc(idx) < len and nums[lc(idx)] > nums[idx]:
            swap(nums, lc(idx), idx)
            max_heapify(nums, lc(idx), len)

    # this converts any binary tree to a max heap
    def converttomaxheap(nums: list[int], len: int):
        for i in range(len // 2, -1, -1): # from len//2 to 0 inc
            max_heapify(nums, i, len)

    converttomaxheap(nums, n) 

    for i in range(n - 1):
        swap(nums, 0, n - 1 - i)

        # the length of our heap (everything at/past this idx is outside our heap)
        limit = n - 1 - i
        max_heapify(nums, 0, limit)

    return nums
```

Ex)
Suppose we start w a list \[1, 17, 2, 5, 20, 15\]

Call converttomaxheap on the list/binary tree (list eq)
we get
- \[20, 17, 15, 5, 1, 2\]
- Now, we swap the 20 with the last element, then we call maxheapify on the index of the 20
- \[2, 17, 15, 5, 1, 20\]
- run maxheapify: \[17, 5, 15, 2, 1, 20]\
- We continue this process, swapping 0 with n-i-1, calling maxheapify on 0 (ignoring elements past n-1-i)

There is a long tree diagram that helps explain this, see justins notes

### Time Complexity + Other

Worst Case:

- ctmh: O(nlgn) on inspection, θ(n) accurate
- csm: n - 1 nodes, θ(1) for swap, θ(1) for chop, O(lg n) for max heapify per node
- so csm for all nodes is, O(nlgn).

All together, heap sort is O(nlgn). With more work, it can be shown to be **θ(nlgn)**.

Best Case:

- A sorted list is actually not fast! We need to make a max heap, which unsorts it
- A max heap is also not as fast, as the second step is still θ(nlgn)
- However, if the entire list is the same element, heap sort is then θ(n)

In Place: Yes, the tree/heap are represented by our regular list
Auxillary space: θ(1)
Stable: No (can you come up with a counter example?)
