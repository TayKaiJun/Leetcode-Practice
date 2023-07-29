def solution(height):
    n = len(height)
    left = 0
    right = n - 1
    container = 0
    while left < right:
        current = min(height[left], height[right]) * (right - left)
        container = max(container, current)
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    return container


if __name__ == "__main__":
    print(solution([1,8,6,2,5,4,8,3,7]))    # 49
    print(solution([8, 7, 3, 3, 7, 8]))     # 40
    print(solution([1,1]))                  # 1
    print(solution([1,2,4,3]))              # 4