def is_sorted(nums: list[int]):
    n = len(nums)

    for i in range(n - 1):
        if nums[i + 1] < nums[i]:
            return False

    return True


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


print(search([1,3,5,6,8,9,25,28,291,434], 4))
