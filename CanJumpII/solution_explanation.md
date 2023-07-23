# Intuition
The intuition behind this solution is that within the steps that are reachable in the current jump, we want to find the step that would give us the furthest reach. Once we do, we **slide** the search region to be the next set of reachable steps, starting from `highest step that the previous jump could reach + 1` till `highest step + furthest reach`.

# Complexity
- Time complexity:
  O(n): we only need to go through the array `nums` once

- Space complexity:
  O(1): only the `left`, `right`, `step`, and `max_reach` variables are needed to track our progress as we slide the reachable window across the array

# Code
```
class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
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
```

Drop comments if you have suggestion on how I can improve this solution or improve my explanation! Thanks!