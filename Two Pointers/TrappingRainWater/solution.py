def solution(height):
    n = len(height)
    if n < 3:
        return 0
    left = 0
    right = 2
    
    sum = 0
    
    def findLocalMax(i):
        """
        starting from i, returns the first index >= i that is greater than height[i]
        TODO: Check right most case
        """
        while i < n-1 and height[i] <= height[i+1]:
            i += 1
        return i if i < n else n-1
    
    while right < n:
        left = findLocalMax(left)
        right = findLocalMax(left + 2)
        
        level = min(height[left], height[right])
        for i in range(left+1, right):
            if height[i] < level:
                sum += level - height[i]
        
        left = right
        right += 2
        
    return sum

if __name__ == "__main__":
    # print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))      # 6
    print(solution([4,2,0,3,2,5]))                  # 9
    # print(solution([0,2,4,0,4,2,0]))                # 4
    # print(solution([0,5,4,1,1,2]))                  # 2
