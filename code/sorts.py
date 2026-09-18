def swap(nums: list[int], i: int, j: int):
    nums[i], nums[j] = nums[j], nums[i]

def bubble(nums: list[int]):
    n = len(nums)

    for i in range(n):
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
