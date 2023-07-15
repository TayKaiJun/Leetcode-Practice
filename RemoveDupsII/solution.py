def solution(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    current = nums[0]
    twice = False
    unique = 1
    nextIndex = 1

    for i in range(1, len(nums)):
        if nums[i] == current and not twice:
            nums[nextIndex] = current
            nextIndex += 1
            twice = True
            unique += 1
            continue
        if nums[i] != current:
            current = nums[i]
            nums[nextIndex] = current
            unique += 1
            nextIndex += 1
            twice = False

    return unique

if __name__ == "__main__":
    # print(solution([1,1,1,2,2,3])) # insert input in the quotes
    print(solution([0,0,1,1,1,1,2,3,3]))
