def solution(nums, target):
    numbers = {}
    n = len(nums)
    for i in range(n):
        if nums[i] not in numbers:
            numbers[nums[i]] = [i]
        else:
            temp = numbers[nums[i]]
            numbers[nums[i]] = temp + [i]
    
    for i in range(n):
        pair = target - nums[i]
        if pair in numbers:
            if pair != nums[i]:
                return [i, numbers[pair][0]]
            elif len(numbers[pair]) >= 2:
                return numbers[pair][:2]

if __name__ == "__main__":
    print(solution([2,7,11,15], 9))     # [0,1]
    print(solution([3,2,4], 6))         # [1,2]
    print(solution([3,3], 6))           # [0,1]