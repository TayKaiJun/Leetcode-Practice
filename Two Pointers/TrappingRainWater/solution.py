def solution(height):
    n = len(height)
    left = 0
    right = n-1
    max_left = float('-inf')
    max_right = float('-inf')
    sum = 0
    
    while left < right:
        if(height[left] < height[right]):
            max_left = max(max_left, height[left])
            sum += max_left - height[left]
            left += 1
        else:
            max_right = max(max_right, height[right])
            sum += max_right - height[right]
            right -= 1
    
    return sum


if __name__ == "__main__":
    print(solution([5,5,1,7,1,1,5,2,7,6]))          # 23
    print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))      # 6
    print(solution([4,2,0,3,2,5]))                  # 9
    print(solution([0,2,4,0,4,2,0]))                # 4
    print(solution([0,5,4,1,1,2]))                  # 2
    print(solution([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])) # 83
    print(solution([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]))  # 26
