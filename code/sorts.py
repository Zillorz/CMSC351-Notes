def swap(nums: list[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]

def bubble(nums: list[int]):
    n = len(nums)

    for i in range(n-1):
        for j in range(n - 1 - i):
            if nums[j] > nums[j + 1]:
                swap(nums, j, j+1)

    return nums

def selection(nums: list[int]):
    n = len(nums)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1, n):
            if nums[j] < nums[min_idx]:
                min_idx = j

        # swap i, i does nothing
        swap(nums, i, min_idx)
    
    return nums

def insertion(nums: list[int]):
    n = len(nums)

    for i in range(1, n):
        j = i

        while j > 0 and nums[j] < nums[j - 1]:
            swap(nums, j, j - 1)
            j -= 1

    return nums

def heap_sort(nums: list[int]):
    n = len(nums)

    # need to create a heap
    # idea, element n has children 2n+1, 2n+2
    # element n has parent (n-1) // 2
    # an element is always larger than it's children
    
    # functions for MUCH better readability
    # p -> parent of node
    # lc -> left child
    # rc -> right child
    def p(i: int): return int((i - 1) / 2)
    def lc(i: int): return 2 * i + 1
    def rc(i: int): return 2 * i + 2


    for i in range(1, n):
        while nums[p(i)] < nums[i]:
            swap(nums, p(i), i)
            i = p(i)

    for i in range(n - 1):
        swap(nums, 0, n - 1 - i)
        # everything past limit is outside of our heap, and in our sorted section
        j = 0
        limit = n - 1 - i

        # We have element j at 0, we need to correctly reposition this in the heap
        # Switch j with the larger child (if any)

        while (lc(j) < limit and nums[lc(j)] > nums[j]) or (rc(j) < limit and nums[rc(j)] > nums[j]):
            if rc(j) < limit:
                if nums[rc(j)] > nums[lc(j)]:
                    swap(nums, rc(j), j)
                    j = rc(j)
                else:
                    swap(nums, lc(j), j)
                    j = lc(j)
            else:
                # at this point, only the left child is a child
                swap(nums, lc(j), j)
                j = lc(j)


    return nums


print(heap_sort([5, 3, 2, -1, 4, 34, -23, 43, 23, 12, 73]))
