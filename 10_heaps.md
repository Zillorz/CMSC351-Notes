# Heaps

Practice: https://leetcode.com/problem-list/heap-priority-queue/ (so so many)
Also: Leetcode 912 (fun fact, this is the first sort fast enough to pass!)

### Binary Trees

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

## Max Heaps
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
    - = Call maxheapify on $\lfloor\frac{n/2}\rfloor \dots 1$
    - We're left with a max heap!

BC: $\theta(n)$, already a max heap, no swaps
WC:
maxheapify is worst case $O(\lg n)$, we call this function on all n nodes, so
$O(n\lg n)$

Note: more precise analysis can get us a worse case bound of $\theta(n)$!
