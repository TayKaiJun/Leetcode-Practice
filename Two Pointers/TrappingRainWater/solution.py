def solution(height):
    n = len(height)
    if n < 3:
        return 0
    left = 0
    right = n-1
    highest_level = 0
    sum = 0
    
    def findLocalMax(i, reversed):
        """
        starting from i, returns the first index >= i that is greater than height[i]
        TODO: Check right most case
        """
        
        if reversed:
            while i > 3 and (height[i] <= height[i-1] or height[i] <= highest_level):
                i -= 1
        else:
            while i < (n-3) and (height[i] <= height[i+1] or height[i] <= highest_level):
                i += 1
        
        return i
    
    left = findLocalMax(left, reversed=False)
    right = findLocalMax(right, reversed=True)
    
    while left < right:
        level = min(height[left], height[right])
        if level <= highest_level:
            if height[left] < height[right]:
                left = findLocalMax(left+1, reversed=False)
            else:
                right = findLocalMax(right-1, reversed=True)
            continue
        
        for i in range(left+1, right):
            if height[i] < level:
                sum += level - max(height[i], highest_level)
        
        if height[left] < height[right]:
            left = findLocalMax(left+1, reversed=False)
        else:
            right = findLocalMax(right-1, reversed=True)
        
        highest_level = level
        
    return sum

if __name__ == "__main__":
    print(solution([5,5,1,7,1,1,5,2,7,6]))          # 23
    print(solution([0,1,0,2,1,0,1,3,2,1,2,1]))      # 6
    print(solution([4,2,0,3,2,5]))                  # 9
    print(solution([0,2,4,0,4,2,0]))                # 4
    print(solution([0,5,4,1,1,2]))                  # 2
    print(solution([6,4,2,0,3,2,0,3,1,4,5,3,2,7,5,3,0,1,2,1,3,4,6,8,1,3])) # 83
                    #     1 3   1 3   2       1       3 2 1 2         2      = 21 (6 & 3)
                    #   2 3 3 3 3 3 3 3 2 1 3 3   1 3 3 3 3 3 3 2            = 53 (6 & 8)
                    #                             1 1 1 1 1 1 1 1 1          = 9  (7 & 8)
                    #                                                        = 83
                    
    print(solution([0,1,2,0,3,0,1,2,0,0,4,2,1,2,5,0,1,2,0,2]))  # 26
                        #   2   2 1   2 2     1     2 1   2       = 15
                        #       1 1 1 1 1   1 1 1
