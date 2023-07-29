def solution(nums):
    answer = []
    nums.sort()

    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if 0 < i < len(nums) - 1 and nums[i] == nums[i - 1]:
            continue

        j = i + 1
        k = len(nums) - 1
        while j < k:
            result = nums[i] + nums[j] + nums[k]
            if result == 0:
                answer.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1
                while (0 < j < len(nums) - 1  and nums[j] == nums[j-1]) and (0 < k < len(nums) - 1 and nums[k] == nums[k+1]):
                    j += 1
                    k -= 1
            elif result < 0:
                j += 1
            else:
                k -= 1
    return answer


if __name__ == "__main__":
    print(solution([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    print(solution([4, -1, -3, -3, 0, 0, 0, 0, 2, 3, 3, 6]))
    print(solution([0, 1, 1]))  # []
    print(solution([0, 0, 0]))  # [0,0,0]
    print(solution([-2, 2, 2, 0, 0, 2, 0, 0]))
