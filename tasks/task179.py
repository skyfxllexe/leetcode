def rotate(nums: int, k: int):
    nums = nums[-1:-k-1:-1][::-1] + nums[:len(nums)-k]
    return nums
print(rotate([1,2,3,4,5,6,7],3))
