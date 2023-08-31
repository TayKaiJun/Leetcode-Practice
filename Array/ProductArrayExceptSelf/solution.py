import math

def solution(nums):
    n = len(nums)
    
    if n == 2:
        return [nums[1], nums[0]]
    
    result = [1] * n
    
    # result[i] stores the product of all numbers up till i-1 (inclusive)
    for i in range(1, n):
        result[i] = result[i-1] * nums[i-1]
    
    last_right = 1
    for i in range(n-1, -1, -1):
        result[i] *= last_right
        last_right *= nums[i]
    
    return result

if __name__ == "__main__":
    print(solution([1,2]))              # [2,1]
    print(solution([1,2,3,4]))          # [24,12,8,6]
    print(solution([-1,1,0,-3,3]))      # [0,0,9,0,0]
