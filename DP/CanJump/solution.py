def canJump(nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    if len(nums) == 1:
        return True

    i = 0
    remainingSteps = nums[0]

    while i < len(nums):
        if nums[i] > remainingSteps:
            remainingSteps = nums[i]

        if remainingSteps == 0:
            break
        else:
            remainingSteps -= 1

        i += 1

    return i >= len(nums)-1


if __name__ == "__main__":
    print(canJump([3,2,1,0,4]))
    print(canJump([2,3,1,1,4]))
    print(canJump([1,2,3]))
    print(canJump([2,0]))
