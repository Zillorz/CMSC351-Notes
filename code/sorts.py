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
    def partition(nums: list[int], left: int, right: int):
        pivot = nums[right]
        print(pivot)

        t = left
        for i in range(t, right):
            if nums[i] <= pivot:
                swap(nums, t, i)
                t += 1

        swap(nums, t, right)
        return t


    def quick_sort_aux(nums: list[int], left: int, right: int):
        if left >= right: return
        
        pivot_idx = partition(nums, left, right)
        quick_sort_aux(nums, left, pivot_idx-1)
        quick_sort_aux(nums, pivot_idx+1, right)

    quick_sort_aux(nums, 0, len(nums) - 1)
    return nums

def counting_sort(nums: list[int]):
    n = len(nums)

    size = max(nums) + 1 # O(N) time!
    pos = [0 for _ in range(size)]

    for num in nums:
        pos[num] += 1

    for i in range(1, size):
        pos[i] = pos[i] + pos[i - 1]

    new_list = [0 for _ in range(n)]
    
    for i in reversed(range(n)):
        value = nums[i]
        new_list[pos[value] - 1] = value
        pos[value] -= 1

    for i in range(n):
        nums[i] = new_list[i]

    return nums

from math import log10

# modified counting sort to help us out for radix
# necessary because we didn't implement sorts on properties
def counting_sort_on_digit(nums: list[int], d: int):
    n = len(nums)

    def get_digit(num: int, d: int):
        return int(num / (10 ** d)) % 10

    size = 10 # 0 through 9
    pos = [0 for _ in range(size)]

    for num in nums:
        pos[get_digit(num, d)] += 1

    for i in range(1, size):
        pos[i] += pos[i - 1]

    new_list = [0 for _ in range(n)]

    for i in reversed(range(n)):
        value = nums[i]
        digit = get_digit(value, d)
        new_list[pos[digit] - 1] = value
        pos[digit] -= 1

    for i in range(n):
        nums[i] = new_list[i]

def radix_sort(nums: list[int]):
    # normally our max-digit count would be passed to us
    d = int(log10(max(nums)) + 1)

    for i in range(d):
        # run our sorting algorithm on the digit D of our list
        counting_sort_on_digit(nums, i)

    return nums


print(radix_sort([23, 6, 34, 23, 5, 6, 35, 35, 24,23, 23,23, 3, 5,6, 2332, 7, 8,87,87, 13, 32,4, 4]))
