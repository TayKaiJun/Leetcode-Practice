def solution(nums):
    n = len(nums)
    left = right = 0


if __name__ == "__main__":
    print(solution([1]))            # 0
    print(solution([3,2,1,4]))      # 1
    print(solution([2,3,1,1,4]))    # 2
    print(solution([2,3,0,1,4]))    # 2
    print(solution([1,2,3]))        # 2
    print(solution([2,0]))          # 1
    print(solution([10,1,1,1,1,1,1,1,1,1,1])) # 1
    print(solution([5,6,4,4,6,9,4,4,7,4,4,8,2,6,8,1,5,9,6,5,2,7,9,7,9,6,9,4,1,6,8,8,4,4,2,0,3,8,5])) # 4
    print(solution([9,8,2,2,0,2,2,0,4,1,5,7,9,6,6,0,6,5,0,5])) # 3
