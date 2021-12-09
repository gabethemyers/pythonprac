


def slow_search(nums, num):
    for i in nums:
        if i == num:
            return True
    return False

def not_binary(nums, num):
    if num in nums:
        return True
    else:
        return False

def binary_search(nums, num):
    nums.sort()
    len_nums = len(nums)
    while len_nums != 1:
        len_nums = len(nums)
        half = len_nums // 2
        if nums[half] == num:
            return True
        elif nums[half] < num:
            nums = nums[half:]
        elif nums[half] > num:
            nums = nums[:half]
    return False




