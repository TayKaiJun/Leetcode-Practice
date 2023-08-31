def solution(gas, cost):
    """
    :type gas: List[int]
    :type cost: List[int]
    :rtype: int
    """
    
    # Idea is that firstly, if the total cost is more than the total gas, this is impossible so return -1
    # Then we break the problem down into segments, where a segment is a continuous subarray of gas and cost
    # such that the sum of the segments will always be negative, except for 1 segment that will be positive
    
    # This works because if we have a segment that is negative, we can't start from any index in that segment
    # because we will always run out of gas before we reach the end of the segment.
    # Thus, we find the segment with the largest positive sum, and return the first index of that segment
    
    if sum(gas) < sum(cost):
        return -1
    
    first_of_segment = [0]
    segment_sum = [0]
    
    for i in range(len(gas)):
        diff = gas[i] - cost[i]
        segment_sum[-1] += diff
        
        if segment_sum[-1] < 0 and i < len(gas) - 1:
            first_of_segment.append(i+1)
            segment_sum.append(0)
        else:
            if i == len(gas) - 1 and len(first_of_segment) > 1:
                first_of_segment.pop(0)
                segment_sum[-1] += segment_sum[0]
                segment_sum.pop(0)
    
    return first_of_segment[segment_sum.index(max(segment_sum))]


if __name__ == "__main__":
    # print(solution([1,2,3,4,5], [3,4,5,1,2]))   # return 3
    # print(solution([2,3,4], [3,4,3]))           # return -1
    # print(solution([5,8,2,8], [6,5,6,6]))       # return 3
    # print(solution([5,1,2,3,4], [4,4,1,5,1]))       # return 4
    # print(solution([1,1,10,1,1], [2,5,1,5,1]))       # return 2
    # print(solution([5,1,2,3,4], [4,4,1,5,1]))       # return 4
    print(solution([3,1,1], [1,2,2]))       # return 0