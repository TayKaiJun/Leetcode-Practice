def solution(nums):
  nums.sort()
  answer = []
  n = len(nums)
  
  def findRight(nums, right):
    right -= 1
    while right > 1 and nums[right] == nums[right+1]:
      right -= 1
    return right
  
  def findLeft(nums, left):
    left += 1
    while left < n-1 and nums[left] == nums[left-1]:
      left += 1
    return left
  
  for i in range(n):
    
    if i > 0 and nums[i] == nums[i-1]:
      # prevent repititons
      continue
    
    if nums[i] >= 0 and nums.count(0) >= 3:
      # if the left most number is 0, the only possible solution is for the next 2 numbers to be 0 too
      answer.append([0,0,0])
      break
    
    left = i+1
    right = n-1
    
    while left < right:
      sum = nums[i] + nums[left] + nums[right]
      if sum == 0:
        answer.append([nums[i], nums[left], nums[right]])
        left = findLeft(nums, left)
        right = findRight(nums, right)
      elif sum < 0:
        left = findLeft(nums, left)
      else:
        right = findRight(nums, right)
  
  return answer
  
  
if __name__ == "__main__":
    # print(solution([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2],[-1,0,1]]
    # print(solution([4, -1, -3, -3, 0, 0, 0, 0, 2, 3, 3, 6])) # [[-3 -3 6], [-3 -1 4], [-3 0 3], [0 0 0]]
    # print(solution([0, 1, 1]))  # []
    # print(solution([0, 0, 0]))  # [0,0,0]
    # print(solution([-2, 2, 2, 0, 0, 2, 0, 0]))
    # print(solution([1,1,-2])) # [-2,1,1]
    print(solution([34,55,79,28,46,33,2,48,31,-3,84,71,52,-3,93,15,21,-43,57,-6,86,56,94,74,83,-14,28,-66,46,-49,62,-11,43,65,77,12,47,61,26,1,13,29,55,-82,76,26,15,-29,36,-29,10,-70,69,17,49]))
    
    #[[-82,-11,93],
    # [-70,-14,84],[-70,-6,76],[-70,1,69],
    # [-66,-11,77],[-66,-3,69],[-66,1,65],
    # [-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],
    # [-43,-14,57],[-43,-6,49],[-43,-3,46],
    # [-29,-14,43],[-29,1,28],[-14,-3,17],[-14,1,13],[-14,2,12],[-11,-6,17],[-11,1,10],[-3,1,2]]
    
    # [[-82,-11,93],[-82,13,69],[-82,17,65],[-82,21,61],[-82,26,56],[-82,33,49],[-82,34,48],[-82,36,46],
    # [-70,-14,84],[-70,-6,76],[-70,1,69],[-70,13,57],[-70,15,55],[-70,21,49],[-70,34,36],
    # [-66,-11,77],[-66,-3,69],[-66,1,65],[-66,10,56],[-66,17,49],
    # [-49,-6,55],[-49,-3,52],[-49,1,48],[-49,2,47],[-49,13,36],[-49,15,34],[-49,21,28],
    # [-43,-14,57],[-43,-6,49],[-43,-3,46],[-43,10,33],[-43,12,31],[-43,15,28],[-43,17,26],
    # [-29,-14,43],[-29,1,28],[-29,12,17],
    # [-14,-3,17],[-14,1,13],[-14,2,12],
    # [-11,-6,17],[-11,1,10],
    # [-3,1,2]]
