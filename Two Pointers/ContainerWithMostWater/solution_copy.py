def solution(height):
    left = 0
    right = len(height) - 1
    max_area = 0
    while left < right:
        base = right - left
        area = base * min(height[left], height[right])
        max_area = max(max_area, area)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_area


if __name__ == "__main__":
    print(solution([1,8,6,2,5,4,8,3,7]))    # 49
    print(solution([8, 7, 3, 3, 7, 8]))     # 40
    print(solution([1,1]))                  # 1
    print(solution([1,2,4,3]))              # 4
    print(solution([2,7,9,9,7,2]))          # 21