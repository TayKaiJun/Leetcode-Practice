def solution(height):
    n = len(height)
    left = n // 2 - 1
    right = n // 2

    container = 0
    while left > 1 or right < n:
        current = min(height[left], height[right]) * (right - left)
        if current > container:
            container = current
        if height[left] < height[right]:
            if left > 0:
                left -= 1
            else:
                right += 1
        else:
            if right < n:
                right += 1
            else:
                left -= 1

    return container

if __name__ == "__main__":
    print(solution([1,8,6,2,5,4,8,3,7])) # 49
    print(solution([8, 7, 3, 3, 7, 8])) # 40
    print(solution([1,1])) # 1
