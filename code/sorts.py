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

def quick_sort(nums: list[int]):
    def quick_sort_aux(nums: list[int], start: int, end: int):
        if start >= end: return

        pivot = end # great pivot selection (use median or random for a real dataset)!

        for i in range(end - 1, start - 1, - 1): # end-1..start
            if nums[i] > nums[pivot]:
                if pivot - 1 == i:
                    swap(nums, pivot, i)
                    pivot -= 1
                else:
                    swap(nums, pivot, pivot - 1)
                    swap(nums, pivot, i)
                    pivot -= 1

        # sort our halves now
        quick_sort_aux(nums, start, pivot-1)
        quick_sort_aux(nums, pivot+1, end)

    quick_sort_aux(nums, 0, len(nums) - 1)
    return nums


print(quick_sort([43, 3, -4, 12, -3, -12, 323, -12, -5434, 13, -13]))



