def isMonotonic(nums):
    flagIncreasing = True
    flagDecreasing = True
    #increasing
    prev = 0
    for i in range(1, len(nums)):
        prev = nums[i-1]
        if prev > nums[i]:
            flagIncreasing = False
        if prev < nums[i]:
            flagDecreasing = False
    return bool(flagDecreasing + flagIncreasing)
print(isMonotonic([1,2,2,2]))