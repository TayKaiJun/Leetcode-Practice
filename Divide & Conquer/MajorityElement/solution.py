def solution(nums):
    original = nums
    nums.sort()
    newList = []
    while len(nums) > 2:
        for i in range(0, len(nums), 2):
            if i+1 >= len(nums) or i+1 < len(nums) and nums[i] == nums[i+1]:
                newList.append(nums[i])
        nums = newList
        newList = []

    if len(nums) == 1:
        return nums[0]
    else:
        return nums[0] if original.count(nums[0]) > original.count(nums[1]) else nums[1]



if __name__ == "__main__":
    print(solution([2,2,1,1,1,2,2])) # insert input in the quotes
    print(solution([6,6,6,7,7]))
    print(solution([2,2,3,3,3,3,2]))

