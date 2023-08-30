def solve(nums, target):
    count = 0 
    l, r = 0, len(nums) - 1
    nums.sort()

    while l < r:
        if nums[l] + nums[r] < target:
            count += r - l
            l += 1
            
        else:
            r -= 1
    return count

print(solve([-1, 1, 2, 3, 1], 2))