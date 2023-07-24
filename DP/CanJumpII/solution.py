def solution(nums):
    n = len(nums)
    if n == 1:
        return 0
    left = 1
    right = nums[0]
    step = 1

    while right < n-1:
        max_reach = 0
        for i in range(left, right+1):
            if nums[i]+i > right:
                max_reach = max(max_reach, nums[i]+i - right)
        left = right + 1
        right += max_reach
        step += 1

    return step


if __name__ == "__main__":
    print(solution([1]))            # 0
    print(solution([3,2,1,4]))      # 1
    print(solution([2,3,1,1,4]))    # 2
    print(solution([2,3,0,1,4]))    # 2
    print(solution([1,2,3]))        # 2
    print(solution([2,0]))          # 1
    print(solution([10,1,1,1,1,1,1,1,1,1,1])) # 1
    print(solution([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5])) # 4
    print(solution([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5])) # 3
