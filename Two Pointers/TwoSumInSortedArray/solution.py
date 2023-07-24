def solution(numbers, target):
    right = len(numbers)-1
    left = 0

    while right > left:
        sum = numbers[left] + numbers[right]
        if sum == target:
            return [left+1, right+1]
        elif sum < target:
            left += 1
        else:
            right -= 1


if __name__ == "__main__":
    print(solution([2, 7, 11, 15], 9))  # [1,2]
    print(solution([2, 3, 4], 6))       # [1,3]
    print(solution([-1, 0], -1))        # [1,2]
