def missing_number(nums):
    n = len(nums) + 1
    return n * (n - 1) // 2 - sum(nums)

print(missing_number([8,10,11,12]))  # Output: 4
